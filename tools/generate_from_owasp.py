#!/usr/bin/env python3
"""Generate the ASVS throughline source from OWASP's official machine-readable data.

This reads the flat JSON export OWASP publishes for an ASVS edition and emits one
throughline item per chapter (a `user_requirement`) and per verification requirement
(a `system_requirement`), grounded chapter -> intent and requirement -> chapter.

Two invariants make re-running safe and faithful:

* **UIDs are permanent.** The mapping from an ASVS clause (its `source_ref`, e.g.
  ``V2.1.1``) to a throughline UID is derived from the items already on disk. Existing
  items are never rewritten; only clauses that have no item yet get a freshly allocated
  UID, in ASVS document order, continuing from the highest number already used. So the
  curated slice that predates this script keeps its exact UIDs and hand-written titles.
* **Deleted clauses are skipped.** OWASP keeps retired clause numbers as
  ``[DELETED, ...]`` tombstones with no level; those are not verification requirements
  and get no item.

Usage:  python tools/generate_from_owasp.py tools/asvs-4.0.3.flat.json

Because existing items are never rewritten, a change to how a *title* is derived cannot
reach the graph through an ordinary run. Applying one is a separate, explicit operation:

    python tools/generate_from_owasp.py --retitle [--dry-run]

which rewrites only those titles still matching the superseded derivation, and leaves
every hand-curated title untouched.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = REPO / "chapters"          # user_requirement, prefix UR
REQS_DIR = REPO / "requirements"          # system_requirement, prefix SR
INTENT = "INT-0001"


def _levels(r: dict) -> int | None:
    """Lowest ASVS level (1/2/3) at which the clause applies, or None if retired."""
    for i, key in enumerate(("level1", "level2", "level3"), start=1):
        if r.get(key, "").strip():
            return i
    return None


_MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_PROACTIVE = re.compile(r"\s*\((?:C\d+(?:,\s*)?)+\)\s*$")
_WS = re.compile(r"\s+")


def clean_text(desc: str) -> str:
    t = _MD_LINK.sub(r"\1", desc.strip())   # [C1](url) -> C1, [text](url) -> text
    t = _PROACTIVE.sub("", t)               # drop trailing proactive-control refs
    return _WS.sub(" ", t).strip()


# The "Verify that" preamble every ASVS clause opens with. The comma is load-bearing:
# a clause reading "Verify that, during the handshake, ..." puts one exactly where the
# space would be, and a pattern anchored on `that\s` misses it and leaves "that" behind.
_PREFIX = re.compile(r"^Verify\s*(?:that)?\s*[,:;]?\s+", re.IGNORECASE)
_ABBREV = re.compile(
    r"(?<![A-Za-z0-9])(?:e\.g|i\.e|etc|vs|cf|approx|resp|incl|Fig|No|Inc|Ltd)\.",
    re.IGNORECASE,
)


def _mask_non_terminators(t: str) -> str:
    """Blank out `.`/`!`/`?` that do not end a sentence, so the first real one is found.

    ASVS clause text is full of full stops that terminate nothing: abbreviations
    (``e.g.``), dotted version numbers (``PKCS#1 v1.5``), and whole sentences quoted or
    parenthesised inside a larger one. Each is replaced by a NUL of the same width, so
    offsets into the masked string index the original unchanged.
    """
    chars = list(t)
    for m in _ABBREV.finditer(t):
        for i in range(m.start(), m.end()):
            if chars[i] == ".":
                chars[i] = "\x00"
    s = "".join(chars)
    s = re.sub(r"(?<=\d)\.(?=\d)", "\x00", s)                   # decimals: v1.5
    s = re.sub(r"(?<=\b[A-Za-z])\.(?=[A-Za-z]\.)", "\x00", s)   # initialisms: U.S.
    s = re.sub(r"(?<=\b[A-Za-z])\.(?=\s*[a-z])", "\x00", s)     # single letter + lower
    out, depth, in_quote = list(s), 0, False
    for i, ch in enumerate(s):
        if ch == '"':
            in_quote = not in_quote
        elif ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if (depth > 0 or in_quote) and out[i] in ".!?":
            out[i] = "\x00"
    return "".join(out)


def short_title(text: str) -> str:
    """A label for the clause: its first complete sentence, minus the preamble.

    Deliberately uncapped. A title is cut at a sentence boundary or not at all, because
    every cheaper rule truncates mid-thought — see `_legacy_short_title`, which split on
    the first ``[,;.]`` and produced labels like ``Sign`` and
    ``Known insecure block modes (i``. Most ASVS clauses are a single sentence, so most
    titles are the whole clause; that is the intended outcome, not an accident.

    Satisfies throughline-source-quality REQ-0001 (a derived title is a complete
    statement) and REQ-0002 (the derivation is deterministic).
    """
    t = _PREFIX.sub("", text.strip())
    t = (t[:1].upper() + t[1:]) if t else t
    m = re.search(r"[.!?](?=\s|$)", _mask_non_terminators(t))
    return (t[:m.start()] if m else t).strip().rstrip(" ,;:")


def _legacy_short_title(text: str) -> str:
    """The title derivation used before the sentence-based one replaced it.

    Kept for exactly one job: `retitle` compares a stored title against this to tell a
    generated title from a hand-curated one, so curation survives the rewrite
    (throughline-source-quality REQ-0005). It is not a fallback — nothing else calls it,
    and it must not be 'fixed'. Delete it once no branch carries legacy titles.
    """
    t = re.sub(r"^Verify(\s+that)?\s+", "", text, flags=re.IGNORECASE)
    t = (t[:1].upper() + t[1:]) if t else t
    clause = re.split(r"[,;.]", t, maxsplit=1)[0].strip()
    if len(clause) > 100:
        clause = clause[:100].rsplit(" ", 1)[0]
    return clause


def _scan_existing(dir_: Path) -> dict[str, str]:
    """Map source_ref -> UID for the items already on disk, and record the max number."""
    ref2uid: dict[str, str] = {}
    for f in dir_.glob("*.yml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        ref = (data.get("attrs") or {}).get("source_ref")
        if ref:
            ref2uid[ref] = data["uid"]
    return ref2uid


def _max_num(ref2uid: dict[str, str], prefix: str) -> int:
    nums = [int(u.split("-")[1]) for u in ref2uid.values() if u.startswith(prefix + "-")]
    return max(nums, default=0)


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        yaml.safe_dump(item, sort_keys=False, allow_unicode=True, width=80),
        encoding="utf-8",
    )


def retitle(dry_run: bool = False) -> int:
    """Rewrite generated titles in place under the current `short_title`.

    An ordinary run never revisits an item that already exists (that is what keeps UIDs
    and curation safe), so a change to the title derivation cannot reach the graph by
    re-running the generator. This is the explicit operation that applies it, and it
    states what it overwrites rather than doing it silently — the shape
    throughline-source-quality REQ-0005 asks for.

    An item is rewritten only if its stored title is exactly what `_legacy_short_title`
    would have produced from its own text. Anything else is a human's work and is left
    alone; `text` is never touched at all.
    """
    changed: list[tuple[str, str, str]] = []
    curated = unchanged = 0
    for f in sorted(REQS_DIR.glob("*.yml")):
        if f.name.startswith("."):
            continue  # .register.yml is the folder manifest, not an item
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        text, old = data.get("text"), data.get("title")
        if not text or not old:
            continue
        if old != _legacy_short_title(text):
            curated += 1  # hand-written, or already migrated — not ours to rewrite
            continue
        new = short_title(text)
        if new == old:
            unchanged += 1
            continue
        changed.append((data["uid"], old, new))
        if not dry_run:
            data["title"] = new
            _dump(f, data)

    for uid, old, new in changed:
        print(f"{uid}\n  - {old}\n  + {new}")
    verb = "would rewrite" if dry_run else "rewrote"
    print(f"\n{verb} {len(changed)} title(s); "
          f"{unchanged} already correct, {curated} left alone (curated or migrated)")
    return 0


def main(src: str) -> int:
    reqs = yaml.safe_load(Path(src).read_text(encoding="utf-8"))["requirements"]

    ch_ref2uid = _scan_existing(CHAPTERS_DIR)
    sr_ref2uid = _scan_existing(REQS_DIR)
    next_ur = _max_num(ch_ref2uid, "UR") + 1
    next_sr = _max_num(sr_ref2uid, "SR") + 1

    # Chapters, in document order.
    seen_ch: list[str] = []
    for r in reqs:
        cid = r["chapter_id"]
        if cid in seen_ch:
            continue
        seen_ch.append(cid)
        if cid in ch_ref2uid:
            continue  # keep the existing (possibly hand-curated) chapter item
        uid = f"UR-{next_ur:04d}"
        next_ur += 1
        ch_ref2uid[cid] = uid
        _dump(CHAPTERS_DIR / f"{uid}.yml", {
            "uid": uid,
            "type": "user_requirement",
            "status": "approved",
            "title": f"{cid} {r['chapter_name']}",
            "text": f"Verification requirements for {r['chapter_name']} ({cid}).",
            "links": [{"target": INTENT, "type": "derives_from"}],
            "attrs": {"source_ref": cid},
        })

    # Verification requirements, in document order.
    written = 0
    for r in reqs:
        ref = r["req_id"]
        level = _levels(r)
        if level is None:
            continue  # [DELETED, ...] tombstone — not a requirement
        if ref in sr_ref2uid:
            continue  # keep the existing item and its curated title, untouched
        uid = f"SR-{next_sr:04d}"
        next_sr += 1
        sr_ref2uid[ref] = uid
        text = clean_text(r["req_description"])
        _dump(REQS_DIR / f"{uid}.yml", {
            "uid": uid,
            "type": "system_requirement",
            "status": "approved",
            "title": short_title(text),
            "text": text,
            "links": [{"target": ch_ref2uid[r["chapter_id"]], "type": "implements"}],
            "attrs": {"source_ref": ref, "level": level},
        })
        written += 1

    print(f"chapters: {len(seen_ch)} total, {len(ch_ref2uid)} mapped")
    print(f"requirements: {written} new items written, {len(sr_ref2uid)} total mapped")
    return 0


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--retitle" in argv:
        argv.remove("--retitle")
        dry = "--dry-run" in argv
        raise SystemExit(retitle(dry_run=dry))
    raise SystemExit(main(argv[0] if argv else str(REPO / "tools/asvs-4.0.3.flat.json")))
