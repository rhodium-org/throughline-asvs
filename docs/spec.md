# OWASP ASVS 5.0.0 — throughline source

This document is **generated from the graph** by `tl docs`; `tl docs --check` gates
it in CI. The prose headings are hand-owned — everything between `tl:*` markers is
injected from the YAML items, so the published spec can never drift from the graph.

This source is a faithful, complete cut of **OWASP ASVS v5.0.0**: every chapter is
a `user_requirement`, and every verification requirement is a `system_requirement`
that `implements` its chapter. The published ASVS number lives in `attrs.source_ref`
(e.g. `V1.1.1`); the ASVS level in `attrs.level`. The throughline UIDs are this
source's own and immutable — a consumer cites a clause as `asvs:SR-0001`, never by its
ASVS number.

It carries
<!-- tl:count type == 'user_requirement' -->
17
<!-- tl:end --> chapters and
<!-- tl:count type == 'system_requirement' -->
345
<!-- tl:end --> verification requirements.

## Purpose

<!-- tl:item INT-0001 -->
**INT-0001 — An application's security is verifiable against a graded, testable baseline** — `intent`, status `approved`

> The OWASP Application Security Verification Standard exists so that an application's security controls can be verified against a normative, level-graded set of requirements — giving developers, testers and procurers a shared baseline rather than ad-hoc judgement.

**source_ref**: ASVS 5.0.0
<!-- tl:end -->

## V1 Encoding and Sanitization

<!-- tl:item UR-0001 -->
**UR-0001 — V1 Encoding and Sanitization** — `user_requirement`, status `approved`

> Verification requirements for Encoding and Sanitization (V1).

*Derives from:* INT-0001

**source_ref**: V1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | Input is decoded or unescaped into a canonical form only once, it is only decoded when encoded data in that form is expected, and that this is done before processing the input further, for example it is not performed after input validation or sanitization |
| SR-0002 | system_requirement | approved | The application performs output encoding and escaping either as a final step before being used by the interpreter for which it is intended or by the interpreter itself |
| SR-0003 | system_requirement | approved | Output encoding for an HTTP response, HTML document, or XML document is relevant for the context required, such as encoding the relevant characters for HTML elements, HTML attributes, HTML comments, CSS, or HTTP header fields, to avoid changing the message or document structure |
| SR-0004 | system_requirement | approved | When dynamically building URLs, untrusted data is encoded according to its context (e.g., URL encoding or base64url encoding for query or path parameters) |
| SR-0005 | system_requirement | approved | Output encoding or escaping is used when dynamically building JavaScript content (including JSON), to avoid changing the message or document structure (to avoid JavaScript and JSON injection) |
| SR-0006 | system_requirement | approved | Data selection or database queries (e.g., SQL, HQL, NoSQL, Cypher) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from SQL Injection and other database injection attacks |
| SR-0007 | system_requirement | approved | The application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding |
| SR-0008 | system_requirement | approved | The application protects against LDAP injection vulnerabilities, or that specific security controls to prevent LDAP injection have been implemented |
| SR-0009 | system_requirement | approved | The application is protected against XPath injection attacks by using query parameterization or precompiled queries |
| SR-0010 | system_requirement | approved | LaTeX processors are configured securely (such as not using the "--shell-escape" flag) and an allowlist of commands is used to prevent LaTeX injection attacks |
| SR-0011 | system_requirement | approved | The application escapes special characters in regular expressions (typically using a backslash) to prevent them from being misinterpreted as metacharacters |
| SR-0012 | system_requirement | approved | The application is protected against CSV and Formula Injection |
| SR-0013 | system_requirement | approved | All untrusted HTML input from WYSIWYG editors or similar is sanitized using a well-known and secure HTML sanitization library or framework feature |
| SR-0014 | system_requirement | approved | The application avoids the use of eval() or other dynamic code execution features such as Spring Expression Language (SpEL) |
| SR-0015 | system_requirement | approved | Data being passed to a potentially dangerous context is sanitized beforehand to enforce safety measures, such as only allowing characters which are safe for this context and trimming input which is too long |
| SR-0016 | system_requirement | approved | User-supplied Scalable Vector Graphics (SVG) scriptable content is validated or sanitized to contain only tags and attributes (such as draw graphics) that are safe for the application, e.g., do not contain scripts and foreignObject |
| SR-0017 | system_requirement | approved | The application sanitizes or disables user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar |
| SR-0018 | system_requirement | approved | The application protects against Server-side Request Forgery (SSRF) attacks, by validating untrusted data against an allowlist of protocols, domains, paths and ports and sanitizing potentially dangerous characters before using the data to call another service |
| SR-0019 | system_requirement | approved | The application protects against template injection attacks by not allowing templates to be built based on untrusted input |
| SR-0020 | system_requirement | approved | The application appropriately sanitizes untrusted input before use in Java Naming and Directory Interface (JNDI) queries and that JNDI is configured securely to prevent JNDI injection attacks |
| SR-0021 | system_requirement | approved | The application sanitizes content before it is sent to memcache to prevent injection attacks |
| SR-0022 | system_requirement | approved | Format strings which might resolve in an unexpected or malicious way when used are sanitized before being processed |
| SR-0023 | system_requirement | approved | The application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection |
| SR-0024 | system_requirement | approved | Regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks |
| SR-0025 | system_requirement | approved | The application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows |
| SR-0026 | system_requirement | approved | Sign, range, and input validation techniques are used to prevent integer overflows |
| SR-0027 | system_requirement | approved | Dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerabilities |
| SR-0028 | system_requirement | approved | The application configures XML parsers to use a restrictive configuration and that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks |
| SR-0029 | system_requirement | approved | Deserialization of untrusted data enforces safe input handling, such as using an allowlist of object types or restricting client-defined object types, to prevent deserialization attacks |
| SR-0030 | system_requirement | approved | Different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks |
<!-- tl:end -->

## V2 Validation and Business Logic

<!-- tl:item UR-0002 -->
**UR-0002 — V2 Validation and Business Logic** — `user_requirement`, status `approved`

> Verification requirements for Validation and Business Logic (V2).

*Derives from:* INT-0001

**source_ref**: V2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0031 | system_requirement | approved | The application's documentation defines input validation rules for how to check the validity of data items against an expected structure |
| SR-0032 | system_requirement | approved | The application's documentation defines how to validate the logical and contextual consistency of combined data items, such as checking that suburb and ZIP code match |
| SR-0033 | system_requirement | approved | Expectations for business logic limits and validations are documented, including both per-user and globally across the application |
| SR-0034 | system_requirement | approved | Input is validated to enforce business or functional expectations for that input |
| SR-0035 | system_requirement | approved | The application is designed to enforce input validation at a trusted service layer |
| SR-0036 | system_requirement | approved | The application ensures that combinations of related data items are reasonable according to the pre-defined rules |
| SR-0037 | system_requirement | approved | The application will only process business logic flows for the same user in the expected sequential step order and without skipping steps |
| SR-0038 | system_requirement | approved | Business logic limits are implemented per the application's documentation to avoid business logic flaws being exploited |
| SR-0039 | system_requirement | approved | Transactions are being used at the business logic level such that either a business logic operation succeeds in its entirety or it is rolled back to the previous correct state |
| SR-0040 | system_requirement | approved | Business logic level locking mechanisms are used to ensure that limited quantity resources (such as theater seats or delivery slots) cannot be double-booked by manipulating the application's logic |
| SR-0041 | system_requirement | approved | High-value business logic flows require multi-user approval to prevent unauthorized or accidental actions |
| SR-0042 | system_requirement | approved | Anti-automation controls are in place to protect against excessive calls to application functions that could lead to data exfiltration, garbage-data creation, quota exhaustion, rate-limit breaches, denial-of-service, or overuse of costly resources |
| SR-0043 | system_requirement | approved | Business logic flows require realistic human timing, preventing excessively rapid transaction submissions |
<!-- tl:end -->

## V3 Web Frontend Security

<!-- tl:item UR-0003 -->
**UR-0003 — V3 Web Frontend Security** — `user_requirement`, status `approved`

> Verification requirements for Web Frontend Security (V3).

*Derives from:* INT-0001

**source_ref**: V3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0044 | system_requirement | approved | Application documentation states the expected security features that browsers using the application must support (such as HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), and other relevant HTTP security mechanisms) |
| SR-0045 | system_requirement | approved | Security controls are in place to prevent browsers from rendering content or functionality in HTTP responses in an incorrect context (e.g., when an API, a user-uploaded file or other resource is requested directly) |
| SR-0046 | system_requirement | approved | Content intended to be displayed as text, rather than rendered as HTML, is handled using safe rendering functions (such as createTextNode or textContent) to prevent unintended execution of content such as HTML or JavaScript |
| SR-0047 | system_requirement | approved | The application avoids DOM clobbering when using client-side JavaScript by employing explicit variable declarations, performing strict type checking, avoiding storing global variables on the document object, and implementing namespace isolation |
| SR-0048 | system_requirement | approved | Cookies have the 'Secure' attribute set, and if the '\__Host-' prefix is not used for the cookie name, the '__Secure-' prefix must be used for the cookie name |
| SR-0049 | system_requirement | approved | Each cookie's 'SameSite' attribute value is set according to the purpose of the cookie, to limit exposure to user interface redress attacks and browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF) |
| SR-0050 | system_requirement | approved | Cookies have the '__Host-' prefix for the cookie name unless they are explicitly designed to be shared with other hosts |
| SR-0051 | system_requirement | approved | If the value of a cookie is not meant to be accessible to client-side scripts (such as a session token), the cookie must have the 'HttpOnly' attribute set and the same value (e. g. session token) must only be transferred to the client via the 'Set-Cookie' header field |
| SR-0052 | system_requirement | approved | When the application writes a cookie, the cookie name and value length combined are not over 4096 bytes |
| SR-0053 | system_requirement | approved | A Strict-Transport-Security header field is included on all responses to enforce an HTTP Strict Transport Security (HSTS) policy |
| SR-0054 | system_requirement | approved | The Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field is a fixed value by the application, or if the Origin HTTP request header field value is used, it is validated against an allowlist of trusted origins |
| SR-0055 | system_requirement | approved | HTTP responses include a Content-Security-Policy response header field which defines directives to ensure the browser only loads and executes trusted content or resources, in order to limit execution of malicious JavaScript |
| SR-0056 | system_requirement | approved | All HTTP responses contain an 'X-Content-Type-Options: nosniff' header field |
| SR-0057 | system_requirement | approved | The application sets a referrer policy to prevent leakage of technically sensitive data to third-party services via the 'Referer' HTTP request header field |
| SR-0058 | system_requirement | approved | The web application uses the frame-ancestors directive of the Content-Security-Policy header field for every HTTP response to ensure that it cannot be embedded by default and that embedding of specific resources is allowed only when necessary |
| SR-0059 | system_requirement | approved | The Content-Security-Policy header field specifies a location to report violations |
| SR-0060 | system_requirement | approved | All HTTP responses that initiate a document rendering (such as responses with Content-Type text/html), include the Cross‑Origin‑Opener‑Policy header field with the same-origin directive or the same-origin-allow-popups directive as required |
| SR-0061 | system_requirement | approved | If the application does not rely on the CORS preflight mechanism to prevent disallowed cross-origin requests to use sensitive functionality, these requests are validated to ensure they originate from the application itself |
| SR-0062 | system_requirement | approved | If the application relies on the CORS preflight mechanism to prevent disallowed cross-origin use of sensitive functionality, it is not possible to call the functionality with a request which does not trigger a CORS-preflight request |
| SR-0063 | system_requirement | approved | HTTP requests to sensitive functionality use appropriate HTTP methods such as POST, PUT, PATCH, or DELETE, and not methods defined by the HTTP specification as "safe" such as HEAD, OPTIONS, or GET |
| SR-0064 | system_requirement | approved | Separate applications are hosted on different hostnames to leverage the restrictions provided by same-origin policy, including how documents or scripts loaded by one origin can interact with resources from another origin and hostname-based restrictions on cookies |
| SR-0065 | system_requirement | approved | Messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid |
| SR-0066 | system_requirement | approved | JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks |
| SR-0067 | system_requirement | approved | Data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks |
| SR-0068 | system_requirement | approved | Authenticated resources (such as images, videos, scripts, and other documents) can be loaded or embedded on behalf of the user only when intended |
| SR-0069 | system_requirement | approved | Client-side assets, such as JavaScript libraries, CSS, or web fonts, are only hosted externally (e.g., on a Content Delivery Network) if the resource is static and versioned and Subresource Integrity (SRI) is used to validate the integrity of the asset |
| SR-0070 | system_requirement | approved | The application only uses client-side technologies which are still supported and considered secure |
| SR-0071 | system_requirement | approved | The application will only automatically redirect the user to a different hostname or domain (which is not controlled by the application) where the destination appears on an allowlist |
| SR-0072 | system_requirement | approved | The application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation |
| SR-0073 | system_requirement | approved | The application's top-level domain (e.g., site.tld) is added to the public preload list for HTTP Strict Transport Security (HSTS) |
| SR-0074 | system_requirement | approved | The application behaves as documented (such as warning the user or blocking access) if the browser used to access the application does not support the expected security features |
<!-- tl:end -->

## V4 API and Web Service

<!-- tl:item UR-0004 -->
**UR-0004 — V4 API and Web Service** — `user_requirement`, status `approved`

> Verification requirements for API and Web Service (V4).

*Derives from:* INT-0001

**source_ref**: V4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0075 | system_requirement | approved | Every HTTP response with a message body contains a Content-Type header field that matches the actual content of the response, including the charset parameter to specify safe character encoding (e.g., UTF-8, ISO-8859-1) according to IANA Media Types, such as "text/", "/+xml" and "/xml" |
| SR-0076 | system_requirement | approved | Only user-facing endpoints (intended for manual web-browser access) automatically redirect from HTTP to HTTPS, while other services or endpoints do not implement transparent redirects |
| SR-0077 | system_requirement | approved | Any HTTP header field used by the application and set by an intermediary layer, such as a load balancer, a web proxy, or a backend-for-frontend service, cannot be overridden by the end-user |
| SR-0078 | system_requirement | approved | Only HTTP methods that are explicitly supported by the application or its API (including OPTIONS during preflight requests) can be used and that unused methods are blocked |
| SR-0079 | system_requirement | approved | Per-message digital signatures are used to provide additional assurance on top of transport protections for requests or transactions which are highly sensitive or which traverse a number of systems |
| SR-0080 | system_requirement | approved | All application components (including load balancers, firewalls, and application servers) determine boundaries of incoming HTTP messages using the appropriate mechanism for the HTTP version to prevent HTTP request smuggling |
| SR-0081 | system_requirement | approved | When generating HTTP messages, the Content-Length header field does not conflict with the length of the content as determined by the framing of the HTTP protocol, in order to prevent request smuggling attacks |
| SR-0082 | system_requirement | approved | The application does not send nor accept HTTP/2 or HTTP/3 messages with connection-specific header fields such as Transfer-Encoding to prevent response splitting and header injection attacks |
| SR-0083 | system_requirement | approved | The application only accepts HTTP/2 and HTTP/3 requests where the header fields and values do not contain any CR (\r), LF (\n), or CRLF (\r\n) sequences, to prevent header injection attacks |
| SR-0084 | system_requirement | approved | If the application (backend or frontend) builds and sends requests, it uses validation, sanitization, or other mechanisms to avoid creating URIs (such as for API calls) or HTTP request header fields (such as Authorization or Cookie), which are too long to be accepted by the receiving component |
| SR-0085 | system_requirement | approved | A query allowlist, depth limiting, amount limiting, or query cost analysis is used to prevent GraphQL or data layer expression Denial of Service (DoS) as a result of expensive, nested queries |
| SR-0086 | system_requirement | approved | GraphQL introspection queries are disabled in the production environment unless the GraphQL API is meant to be used by other parties |
| SR-0087 | system_requirement | approved | WebSocket over TLS (WSS) is used for all WebSocket connections |
| SR-0088 | system_requirement | approved | During the initial HTTP WebSocket handshake, the Origin header field is checked against a list of origins allowed for the application |
| SR-0089 | system_requirement | approved | If the application's standard session management cannot be used, dedicated tokens are being used for this, which comply with the relevant Session Management security requirements |
| SR-0090 | system_requirement | approved | Dedicated WebSocket session management tokens are initially obtained or validated through the previously authenticated HTTPS session when transitioning an existing HTTPS session to a WebSocket channel |
<!-- tl:end -->

## V5 File Handling

<!-- tl:item UR-0005 -->
**UR-0005 — V5 File Handling** — `user_requirement`, status `approved`

> Verification requirements for File Handling (V5).

*Derives from:* INT-0001

**source_ref**: V5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0091 | system_requirement | approved | The documentation defines the permitted file types, expected file extensions, and maximum size (including unpacked size) for each upload feature |
| SR-0092 | system_requirement | approved | The application will only accept files of a size which it can process without causing a loss of performance or a denial of service attack |
| SR-0093 | system_requirement | approved | When the application accepts a file, either on its own or within an archive such as a zip file, it checks if the file extension matches an expected file extension and validates that the contents correspond to the type represented by the extension |
| SR-0094 | system_requirement | approved | The application checks compressed files (e.g., zip, gz, docx, odt) against maximum allowed uncompressed size and against maximum number of files before uncompressing the file |
| SR-0095 | system_requirement | approved | A file size quota and maximum number of files per user are enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files |
| SR-0096 | system_requirement | approved | The application does not allow uploading compressed files containing symlinks unless this is specifically required (in which case it will be necessary to enforce an allowlist of the files that can be symlinked to) |
| SR-0097 | system_requirement | approved | The application rejects uploaded images with a pixel size larger than the maximum allowed, to prevent pixel flood attacks |
| SR-0098 | system_requirement | approved | Files uploaded or generated by untrusted input and stored in a public folder, are not executed as server-side program code when accessed directly with an HTTP request |
| SR-0099 | system_requirement | approved | When the application creates file paths for file operations, instead of user-submitted filenames, it uses internally generated or trusted data, or if user-submitted filenames or file metadata must be used, strict validation and sanitization must be applied |
| SR-0100 | system_requirement | approved | Server-side file processing, such as file decompression, ignores user-provided path information to prevent vulnerabilities such as zip slip |
| SR-0101 | system_requirement | approved | The application validates or ignores user-submitted filenames, including in a JSON, JSONP, or URL parameter and specifies a filename in the Content-Disposition header field in the response |
| SR-0102 | system_requirement | approved | File names served (e.g., in HTTP response header fields or email attachments) are encoded or sanitized (e.g., following RFC 6266) to preserve document structure and prevent injection attacks |
| SR-0103 | system_requirement | approved | Files obtained from untrusted sources are scanned by antivirus scanners to prevent serving of known malicious content |
<!-- tl:end -->

## V6 Authentication

<!-- tl:item UR-0006 -->
**UR-0006 — V6 Authentication** — `user_requirement`, status `approved`

> Verification requirements for Authentication (V6).

*Derives from:* INT-0001

**source_ref**: V6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V6.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0104 | system_requirement | approved | Application documentation defines how controls such as rate limiting, anti-automation, and adaptive response, are used to defend against attacks such as credential stuffing and password brute force |
| SR-0105 | system_requirement | approved | A list of context-specific words is documented in order to prevent their use in passwords |
| SR-0106 | system_requirement | approved | If the application includes multiple authentication pathways, these are all documented together with the security controls and authentication strength which must be consistently enforced across them |
| SR-0107 | system_requirement | approved | User set passwords are at least 8 characters in length although a minimum of 15 characters is strongly recommended |
| SR-0108 | system_requirement | approved | Users can change their password |
| SR-0109 | system_requirement | approved | Password change functionality requires the user's current and new password |
| SR-0110 | system_requirement | approved | Passwords submitted during account registration or password change are checked against an available set of, at least, the top 3000 passwords which match the application's password policy, e.g. minimum length |
| SR-0111 | system_requirement | approved | Passwords of any composition can be used, without rules limiting the type of characters permitted |
| SR-0112 | system_requirement | approved | Password input fields use type=password to mask the entry |
| SR-0113 | system_requirement | approved | "paste" functionality, browser password helpers, and external password managers are permitted |
| SR-0114 | system_requirement | approved | The application verifies the user's password exactly as received from the user, without any modifications such as truncation or case transformation |
| SR-0115 | system_requirement | approved | Passwords of at least 64 characters are permitted |
| SR-0116 | system_requirement | approved | A user's password stays valid until it is discovered to be compromised or the user rotates it |
| SR-0117 | system_requirement | approved | The documented list of context specific words is used to prevent easy to guess passwords being created |
| SR-0118 | system_requirement | approved | Passwords submitted during account registration or password changes are checked against a set of breached passwords |
| SR-0119 | system_requirement | approved | Controls to prevent attacks such as credential stuffing and password brute force are implemented according to the application's security documentation |
| SR-0120 | system_requirement | approved | Default user accounts (e.g., "root", "admin", or "sa") are not present in the application or are disabled |
| SR-0121 | system_requirement | approved | Either a multi-factor authentication mechanism or a combination of single-factor authentication mechanisms, must be used in order to access the application |
| SR-0122 | system_requirement | approved | If the application includes multiple authentication pathways, there are no undocumented pathways and that security controls and authentication strength are enforced consistently |
| SR-0123 | system_requirement | approved | Users are notified of suspicious authentication attempts (successful or unsuccessful) |
| SR-0124 | system_requirement | approved | Email is not used as either a single-factor or multi-factor authentication mechanism |
| SR-0125 | system_requirement | approved | Users are notified after updates to authentication details, such as credential resets or modification of the username or email address |
| SR-0126 | system_requirement | approved | Valid users cannot be deduced from failed authentication challenges, such as by basing on error messages, HTTP response codes, or different response times |
| SR-0127 | system_requirement | approved | System generated initial passwords or activation codes are securely randomly generated, follow the existing password policy, and expire after a short period of time or after they are initially used |
| SR-0128 | system_requirement | approved | Password hints or knowledge-based authentication (so-called "secret questions") are not present |
| SR-0129 | system_requirement | approved | A secure process for resetting a forgotten password is implemented, that does not bypass any enabled multi-factor authentication mechanisms |
| SR-0130 | system_requirement | approved | If a multi-factor authentication factor is lost, evidence of identity proofing is performed at the same level as during enrollment |
| SR-0131 | system_requirement | approved | Renewal instructions for authentication mechanisms which expire are sent with enough time to be carried out before the old authentication mechanism expires, configuring automated reminders if necessary |
| SR-0132 | system_requirement | approved | Administrative users can initiate the password reset process for the user, but that this does not allow them to change or choose the user's password |
| SR-0133 | system_requirement | approved | Lookup secrets, out-of-band authentication requests or codes, and time-based one-time passwords (TOTPs) are only successfully usable once |
| SR-0134 | system_requirement | approved | When being stored in the application's backend, lookup secrets with less than 112 bits of entropy (19 random alphanumeric characters or 34 random digits) are hashed with an approved password storage hashing algorithm that incorporates a 32-bit random salt |
| SR-0135 | system_requirement | approved | Lookup secrets, out-of-band authentication code, and time-based one-time password seeds, are generated using a Cryptographically Secure Pseudorandom Number Generator (CSPRNG) to avoid predictable values |
| SR-0136 | system_requirement | approved | Lookup secrets and out-of-band authentication codes have a minimum of 20 bits of entropy (typically 4 random alphanumeric characters or 6 random digits is sufficient) |
| SR-0137 | system_requirement | approved | Out-of-band authentication requests, codes, or tokens, as well as time-based one-time passwords (TOTPs) have a defined lifetime |
| SR-0138 | system_requirement | approved | Any authentication factor (including physical devices) can be revoked in case of theft or other loss |
| SR-0139 | system_requirement | approved | Biometric authentication mechanisms are only used as secondary factors together with either something you have or something you know |
| SR-0140 | system_requirement | approved | Time-based one-time passwords (TOTPs) are checked based on a time source from a trusted service and not from an untrusted or client provided time |
| SR-0141 | system_requirement | approved | Authentication mechanisms using the Public Switched Telephone Network (PSTN) to deliver One-time Passwords (OTPs) via phone or SMS are offered only when the phone number has previously been validated, alternate stronger methods (such as Time based One-time Passwords) are also offered, and the service provides information on their security risks to users |
| SR-0142 | system_requirement | approved | Out-of-band authentication requests, codes, or tokens are bound to the original authentication request for which they were generated and are not usable for a previous or subsequent one |
| SR-0143 | system_requirement | approved | A code based out-of-band authentication mechanism is protected against brute force attacks by using rate limiting |
| SR-0144 | system_requirement | approved | Where push notifications are used for multi-factor authentication, rate limiting is used to prevent push bombing attacks |
| SR-0145 | system_requirement | approved | The certificates used to verify cryptographic authentication assertions are stored in a way protects them from modification |
| SR-0146 | system_requirement | approved | The challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device |
| SR-0147 | system_requirement | approved | If the application supports multiple identity providers (IdPs), the user's identity cannot be spoofed via another supported identity provider (eg. by using the same user identifier) |
| SR-0148 | system_requirement | approved | The presence and integrity of digital signatures on authentication assertions (for example on JWTs or SAML assertions) are always validated, rejecting any assertions that are unsigned or have invalid signatures |
| SR-0149 | system_requirement | approved | SAML assertions are uniquely processed and used only once within the validity period to prevent replay attacks |
| SR-0150 | system_requirement | approved | If an application uses a separate Identity Provider (IdP) and expects specific authentication strength, methods, or recentness for specific functions, the application verifies this using the information returned by the IdP |
<!-- tl:end -->

## V7 Session Management

<!-- tl:item UR-0007 -->
**UR-0007 — V7 Session Management** — `user_requirement`, status `approved`

> Verification requirements for Session Management (V7).

*Derives from:* INT-0001

**source_ref**: V7
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V7.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0151 | system_requirement | approved | The user's session inactivity timeout and absolute maximum session lifetime are documented, are appropriate in combination with other controls, and that the documentation includes justification for any deviations from NIST SP 800-63B re-authentication requirements |
| SR-0152 | system_requirement | approved | The documentation defines how many concurrent (parallel) sessions are allowed for one account as well as the intended behaviors and actions to be taken when the maximum number of active sessions is reached |
| SR-0153 | system_requirement | approved | All systems that create and manage user sessions as part of a federated identity management ecosystem (such as SSO systems) are documented along with controls to coordinate session lifetimes, termination, and any other conditions that require re-authentication |
| SR-0154 | system_requirement | approved | The application performs all session token verification using a trusted, backend service |
| SR-0155 | system_requirement | approved | The application uses either self-contained or reference tokens that are dynamically generated for session management, i.e. not using static API secrets and keys |
| SR-0156 | system_requirement | approved | If reference tokens are used to represent user sessions, they are unique and generated using a cryptographically secure pseudo-random number generator (CSPRNG) and possess at least 128 bits of entropy |
| SR-0157 | system_requirement | approved | The application generates a new session token on user authentication, including re-authentication, and terminates the current session token |
| SR-0158 | system_requirement | approved | There is an inactivity timeout such that re-authentication is enforced according to risk analysis and documented security decisions |
| SR-0159 | system_requirement | approved | There is an absolute maximum session lifetime such that re-authentication is enforced according to risk analysis and documented security decisions |
| SR-0160 | system_requirement | approved | When session termination is triggered (such as logout or expiration), the application disallows any further use of the session |
| SR-0161 | system_requirement | approved | The application terminates all active sessions when a user account is disabled or deleted (such as an employee leaving the company) |
| SR-0162 | system_requirement | approved | The application gives the option to terminate all other active sessions after a successful change or removal of any authentication factor (including password change via reset or recovery and, if present, an MFA settings update) |
| SR-0163 | system_requirement | approved | All pages that require authentication have easy and visible access to logout functionality |
| SR-0164 | system_requirement | approved | Application administrators are able to terminate active sessions for an individual user or for all users |
| SR-0165 | system_requirement | approved | The application requires full re-authentication before allowing modifications to sensitive account attributes which may affect authentication such as email address, phone number, MFA configuration, or other information used in account recovery |
| SR-0166 | system_requirement | approved | Users are able to view and (having authenticated again with at least one factor) terminate any or all currently active sessions |
| SR-0167 | system_requirement | approved | The application requires further authentication with at least one factor or secondary verification before performing highly sensitive transactions or operations |
| SR-0168 | system_requirement | approved | Session lifetime and termination between Relying Parties (RPs) and Identity Providers (IdPs) behave as documented, requiring re-authentication as necessary such as when the maximum time between IdP authentication events is reached |
| SR-0169 | system_requirement | approved | Creation of a session requires either the user's consent or an explicit action, preventing the creation of new application sessions without user interaction |
<!-- tl:end -->

## V8 Authorization

<!-- tl:item UR-0008 -->
**UR-0008 — V8 Authorization** — `user_requirement`, status `approved`

> Verification requirements for Authorization (V8).

*Derives from:* INT-0001

**source_ref**: V8
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V8.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0170 | system_requirement | approved | Authorization documentation defines rules for restricting function-level and data-specific access based on consumer permissions and resource attributes |
| SR-0171 | system_requirement | approved | Authorization documentation defines rules for field-level access restrictions (both read and write) based on consumer permissions and resource attributes |
| SR-0172 | system_requirement | approved | The application's documentation defines the environmental and contextual attributes (including but not limited to, time of day, user location, IP address, or device) that are used in the application to make security decisions, including those pertaining to authentication and authorization |
| SR-0173 | system_requirement | approved | Authentication and authorization documentation defines how environmental and contextual factors are used in decision-making, in addition to function-level, data-specific, and field-level authorization |
| SR-0174 | system_requirement | approved | The application ensures that function-level access is restricted to consumers with explicit permissions |
| SR-0175 | system_requirement | approved | The application ensures that data-specific access is restricted to consumers with explicit permissions to specific data items to mitigate insecure direct object reference (IDOR) and broken object level authorization (BOLA) |
| SR-0176 | system_requirement | approved | The application ensures that field-level access is restricted to consumers with explicit permissions to specific fields to mitigate broken object property level authorization (BOPLA) |
| SR-0177 | system_requirement | approved | Adaptive security controls based on a consumer's environmental and contextual attributes (such as time of day, location, IP address, or device) are implemented for authentication and authorization decisions, as defined in the application's documentation |
| SR-0178 | system_requirement | approved | The application enforces authorization rules at a trusted service layer and doesn't rely on controls that an untrusted consumer could manipulate, such as client-side JavaScript |
| SR-0179 | system_requirement | approved | Changes to values on which authorization decisions are made are applied immediately |
| SR-0180 | system_requirement | approved | Access to an object is based on the originating subject's (e.g. consumer's) permissions, not on the permissions of any intermediary or service acting on their behalf |
| SR-0181 | system_requirement | approved | Multi-tenant applications use cross-tenant controls to ensure consumer operations will never affect tenants with which they do not have permissions to interact |
| SR-0182 | system_requirement | approved | Access to administrative interfaces incorporates multiple layers of security, including continuous consumer identity verification, device security posture assessment, and contextual risk analysis, ensuring that network location or trusted endpoints are not the sole factors for authorization even though they may reduce the likelihood of unauthorized access |
<!-- tl:end -->

## V9 Self-contained Tokens

<!-- tl:item UR-0009 -->
**UR-0009 — V9 Self-contained Tokens** — `user_requirement`, status `approved`

> Verification requirements for Self-contained Tokens (V9).

*Derives from:* INT-0001

**source_ref**: V9
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V9.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0183 | system_requirement | approved | Self-contained tokens are validated using their digital signature or MAC to protect against tampering before accepting the token's contents |
| SR-0184 | system_requirement | approved | Only algorithms on an allowlist can be used to create and verify self-contained tokens, for a given context |
| SR-0185 | system_requirement | approved | Key material that is used to validate self-contained tokens is from trusted pre-configured sources for the token issuer, preventing attackers from specifying untrusted sources and keys |
| SR-0186 | system_requirement | approved | If a validity time span is present in the token data, the token and its content are accepted only if the verification time is within this validity time span |
| SR-0187 | system_requirement | approved | The service receiving a token validates the token to be the correct type and is meant for the intended purpose before accepting the token's contents |
| SR-0188 | system_requirement | approved | The service only accepts tokens which are intended for use with that service (audience) |
| SR-0189 | system_requirement | approved | If a token issuer uses the same private key for issuing tokens to different audiences, the issued tokens contain an audience restriction that uniquely identifies the intended audiences |
<!-- tl:end -->

## V10 OAuth and OIDC

<!-- tl:item UR-0010 -->
**UR-0010 — V10 OAuth and OIDC** — `user_requirement`, status `approved`

> Verification requirements for OAuth and OIDC (V10).

*Derives from:* INT-0001

**source_ref**: V10
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V10.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0190 | system_requirement | approved | Tokens are only sent to components that strictly need them |
| SR-0191 | system_requirement | approved | The client only accepts values from the authorization server (such as the authorization code or ID Token) if these values result from an authorization flow that was initiated by the same user agent session and transaction |
| SR-0192 | system_requirement | approved | If the code flow is used, the OAuth client has protection against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF), which trigger token requests, either by using proof key for code exchange (PKCE) functionality or checking the 'state' parameter that was sent in the authorization request |
| SR-0193 | system_requirement | approved | If the OAuth client can interact with more than one authorization server, it has a defense against mix-up attacks |
| SR-0194 | system_requirement | approved | The OAuth client only requests the required scopes (or other authorization parameters) in requests to the authorization server |
| SR-0195 | system_requirement | approved | The resource server only accepts access tokens that are intended for use with that service (audience) |
| SR-0196 | system_requirement | approved | The resource server enforces authorization decisions based on claims from the access token that define delegated authorization |
| SR-0197 | system_requirement | approved | If an access control decision requires identifying a unique user from an access token (JWT or related token introspection response), the resource server identifies the user from claims that cannot be reassigned to other users |
| SR-0198 | system_requirement | approved | If the resource server requires specific authentication strength, methods, or recentness, it verifies that the presented access token satisfies these constraints |
| SR-0199 | system_requirement | approved | The resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP) |
| SR-0200 | system_requirement | approved | The authorization server validates redirect URIs based on a client-specific allowlist of pre-registered URIs using exact string comparison |
| SR-0201 | system_requirement | approved | If the authorization server returns the authorization code in the authorization response, it can be used only once for a token request |
| SR-0202 | system_requirement | approved | The authorization code is short-lived |
| SR-0203 | system_requirement | approved | For a given client, the authorization server only allows the usage of grants that this client needs to use |
| SR-0204 | system_requirement | approved | The authorization server mitigates refresh token replay attacks for public clients, preferably using sender-constrained refresh tokens, i.e., Demonstrating Proof of Possession (DPoP) or Certificate-Bound Access Tokens using mutual TLS (mTLS) |
| SR-0205 | system_requirement | approved | If the code grant is used, the authorization server mitigates authorization code interception attacks by requiring proof key for code exchange (PKCE) |
| SR-0206 | system_requirement | approved | If the authorization server supports unauthenticated dynamic client registration, it mitigates the risk of malicious client applications |
| SR-0207 | system_requirement | approved | Refresh tokens have an absolute expiration, including if sliding refresh token expiration is applied |
| SR-0208 | system_requirement | approved | Refresh tokens and reference access tokens can be revoked by an authorized user using the authorization server user interface, to mitigate the risk of malicious clients or stolen tokens |
| SR-0209 | system_requirement | approved | Confidential client is authenticated for client-to-authorized server backchannel requests such as token requests, pushed authorization requests (PAR), and token revocation requests |
| SR-0210 | system_requirement | approved | The authorization server configuration only assigns the required scopes to the OAuth client |
| SR-0211 | system_requirement | approved | For a given client, the authorization server only allows the 'response_mode' value that this client needs to use |
| SR-0212 | system_requirement | approved | Grant type 'code' is always used together with pushed authorization requests (PAR) |
| SR-0213 | system_requirement | approved | The authorization server issues only sender-constrained (Proof-of-Possession) access tokens, either with certificate-bound access tokens using mutual TLS (mTLS) or DPoP-bound access tokens (Demonstration of Proof of Possession) |
| SR-0214 | system_requirement | approved | For a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it |
| SR-0215 | system_requirement | approved | The client is confidential and the authorization server requires the use of strong client authentication methods (based on public-key cryptography and resistant to replay attacks), such as mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') or private key JWT ('private_key_jwt') |
| SR-0216 | system_requirement | approved | The client (as the relying party) mitigates ID Token replay attacks |
| SR-0217 | system_requirement | approved | The client uniquely identifies the user from ID Token claims, usually the 'sub' claim, which cannot be reassigned to other users (for the scope of an identity provider) |
| SR-0218 | system_requirement | approved | The client rejects attempts by a malicious authorization server to impersonate another authorization server through authorization server metadata |
| SR-0219 | system_requirement | approved | The client validates that the ID Token is intended to be used for that client (audience) by checking that the 'aud' claim from the token is equal to the 'client_id' value for the client |
| SR-0220 | system_requirement | approved | When using OIDC back-channel logout, the relying party mitigates denial of service through forced logout and cross-JWT confusion in the logout flow |
| SR-0221 | system_requirement | approved | The OpenID Provider only allows values 'code', 'ciba', 'id_token', or 'id_token code' for response mode |
| SR-0222 | system_requirement | approved | The OpenID Provider mitigates denial of service through forced logout |
| SR-0223 | system_requirement | approved | The authorization server ensures that the user consents to each authorization request |
| SR-0224 | system_requirement | approved | When the authorization server prompts for user consent, it presents sufficient and clear information about what is being consented to |
| SR-0225 | system_requirement | approved | The user can review, modify, and revoke consents which the user has granted through the authorization server |
<!-- tl:end -->

## V11 Cryptography

<!-- tl:item UR-0011 -->
**UR-0011 — V11 Cryptography** — `user_requirement`, status `approved`

> Verification requirements for Cryptography (V11).

*Derives from:* INT-0001

**source_ref**: V11
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V11.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0226 | system_requirement | approved | There is a documented policy for management of cryptographic keys and a cryptographic key lifecycle that follows a key management standard such as NIST SP 800-57 |
| SR-0227 | system_requirement | approved | A cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application |
| SR-0228 | system_requirement | approved | Cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations |
| SR-0229 | system_requirement | approved | A cryptographic inventory is maintained |
| SR-0230 | system_requirement | approved | Industry-validated implementations (including libraries and hardware-accelerated implementations) are used for cryptographic operations |
| SR-0231 | system_requirement | approved | The application is designed with crypto agility such that random number, authenticated encryption, MAC, or hashing algorithms, key lengths, rounds, ciphers and modes can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks |
| SR-0232 | system_requirement | approved | All cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm, key size, and configuration |
| SR-0233 | system_requirement | approved | All cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information |
| SR-0234 | system_requirement | approved | All cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities, such as Padding Oracle attacks |
| SR-0235 | system_requirement | approved | Insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used |
| SR-0236 | system_requirement | approved | Only approved ciphers and modes such as AES with GCM are used |
| SR-0237 | system_requirement | approved | Encrypted data is protected against unauthorized modification preferably by using an approved authenticated encryption method or by combining an approved encryption method with an approved MAC algorithm |
| SR-0238 | system_requirement | approved | Nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair |
| SR-0239 | system_requirement | approved | Any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode |
| SR-0240 | system_requirement | approved | Only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation |
| SR-0241 | system_requirement | approved | Passwords are stored using an approved, computationally intensive, key derivation function (also known as a "password hashing function"), with parameter settings configured based on current guidance |
| SR-0242 | system_requirement | approved | Hash functions used in digital signatures, as part of data authentication or data integrity are collision resistant and have appropriate bit-lengths |
| SR-0243 | system_requirement | approved | The application uses approved key derivation functions with key stretching parameters when deriving secret keys from passwords |
| SR-0244 | system_requirement | approved | All random numbers and strings which are intended to be non-guessable must be generated using a cryptographically secure pseudo-random number generator (CSPRNG) and have at least 128 bits of entropy |
| SR-0245 | system_requirement | approved | The random number generation mechanism in use is designed to work securely, even under heavy demand |
| SR-0246 | system_requirement | approved | Only approved cryptographic algorithms and modes of operation are used for key generation and seeding, and digital signature generation and verification |
| SR-0247 | system_requirement | approved | Approved cryptographic algorithms are used for key exchange (such as Diffie-Hellman) with a focus on ensuring that key exchange mechanisms use secure parameters |
| SR-0248 | system_requirement | approved | Full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes |
| SR-0249 | system_requirement | approved | Data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible |
<!-- tl:end -->

## V12 Secure Communication

<!-- tl:item UR-0012 -->
**UR-0012 — V12 Secure Communication** — `user_requirement`, status `approved`

> Verification requirements for Secure Communication (V12).

*Derives from:* INT-0001

**source_ref**: V12
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V12.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0250 | system_requirement | approved | Only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3 |
| SR-0251 | system_requirement | approved | Only recommended cipher suites are enabled, with the strongest cipher suites set as preferred |
| SR-0252 | system_requirement | approved | The application validates that mTLS client certificates are trusted before using the certificate identity for authentication or authorization |
| SR-0253 | system_requirement | approved | Proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured |
| SR-0254 | system_requirement | approved | Encrypted Client Hello (ECH) is enabled in the application's TLS settings to prevent exposure of sensitive metadata, such as the Server Name Indication (SNI), during TLS handshake processes |
| SR-0255 | system_requirement | approved | TLS is used for all connectivity between a client and external facing, HTTP-based services, and does not fall back to insecure or unencrypted communications |
| SR-0256 | system_requirement | approved | External facing services use publicly trusted TLS certificates |
| SR-0257 | system_requirement | approved | An encrypted protocol such as TLS is used for all inbound and outbound connections to and from the application, including monitoring systems, management tools, remote access and SSH, middleware, databases, mainframes, partner systems, or external APIs |
| SR-0258 | system_requirement | approved | TLS clients validate certificates received before communicating with a TLS server |
| SR-0259 | system_requirement | approved | TLS or another appropriate transport encryption mechanism used for all connectivity between internal, HTTP-based services within the application, and does not fall back to insecure or unencrypted communications |
| SR-0260 | system_requirement | approved | TLS connections between internal services use trusted certificates |
| SR-0261 | system_requirement | approved | Services communicating internally within a system (intra-service communications) use strong authentication to ensure that each endpoint is verified |
<!-- tl:end -->

## V13 Configuration

<!-- tl:item UR-0013 -->
**UR-0013 — V13 Configuration** — `user_requirement`, status `approved`

> Verification requirements for Configuration (V13).

*Derives from:* INT-0001

**source_ref**: V13
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V13.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0262 | system_requirement | approved | All communication needs for the application are documented |
| SR-0263 | system_requirement | approved | For each service the application uses, the documentation defines the maximum number of concurrent connections (e.g., connection pool limits) and how the application behaves when that limit is reached, including any fallback or recovery mechanisms, to prevent denial of service conditions |
| SR-0264 | system_requirement | approved | The application documentation defines resource‑management strategies for every external system or service it uses (e.g., databases, file handles, threads, HTTP connections) |
| SR-0265 | system_requirement | approved | The application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and business requirements |
| SR-0266 | system_requirement | approved | Communications between backend application components that don't support the application's standard user session mechanism, including APIs, middleware, and data layers, are authenticated |
| SR-0267 | system_requirement | approved | Communications between backend application components, including local or operating system services, APIs, middleware, and data layers, are performed with accounts assigned the least necessary privileges |
| SR-0268 | system_requirement | approved | If a credential has to be used for service authentication, the credential being used by the consumer is not a default credential (e.g., root/root or admin/admin) |
| SR-0269 | system_requirement | approved | An allowlist is used to define the external resources or systems with which the application is permitted to communicate (e.g., for outbound requests, data loads, or file access) |
| SR-0270 | system_requirement | approved | The web or application server is configured with an allowlist of resources or systems to which the server can send requests or load data or files from |
| SR-0271 | system_requirement | approved | Where the application connects to separate services, it follows the documented configuration for each connection, such as maximum parallel connections, behavior when maximum allowed connections is reached, connection timeouts, and retry strategies |
| SR-0272 | system_requirement | approved | A secrets management solution, such as a key vault, is used to securely create, store, control access to, and destroy backend secrets |
| SR-0273 | system_requirement | approved | Access to secret assets adheres to the principle of least privilege |
| SR-0274 | system_requirement | approved | All cryptographic operations are performed using an isolated security module (such as a vault or hardware security module) to securely manage and protect key material from exposure outside of the security module |
| SR-0275 | system_requirement | approved | Secrets are configured to expire and be rotated based on the application's documentation |
| SR-0276 | system_requirement | approved | The application is deployed either without any source control metadata, including the .git or .svn folders, or in a way that these folders are inaccessible both externally and to the application itself |
| SR-0277 | system_requirement | approved | Debug modes are disabled for all components in production environments to prevent exposure of debugging features and information leakage |
| SR-0278 | system_requirement | approved | Web servers do not expose directory listings to clients unless explicitly intended |
| SR-0279 | system_requirement | approved | Using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage |
| SR-0280 | system_requirement | approved | Documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended |
| SR-0281 | system_requirement | approved | The application does not expose detailed version information of backend components |
| SR-0282 | system_requirement | approved | The web tier is configured to only serve files with specific file extensions to prevent unintentional information, configuration, and source code leakage |
<!-- tl:end -->

## V14 Data Protection

<!-- tl:item UR-0014 -->
**UR-0014 — V14 Data Protection** — `user_requirement`, status `approved`

> Verification requirements for Data Protection (V14).

*Derives from:* INT-0001

**source_ref**: V14
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V14.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0283 | system_requirement | approved | All sensitive data created and processed by the application has been identified and classified into protection levels |
| SR-0284 | system_requirement | approved | All sensitive data protection levels have a documented set of protection requirements |
| SR-0285 | system_requirement | approved | Sensitive data is only sent to the server in the HTTP message body or header fields, and that the URL and query string do not contain sensitive information, such as an API key or session token |
| SR-0286 | system_requirement | approved | The application prevents sensitive data from being cached in server components, such as load balancers and application caches, or ensures that the data is securely purged after use |
| SR-0287 | system_requirement | approved | Defined sensitive data is not sent to untrusted parties (e.g., user trackers) to prevent unwanted collection of data outside of the application's control |
| SR-0288 | system_requirement | approved | Controls around sensitive data related to encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, privacy and privacy-enhancing technologies, are implemented as defined in the documentation for the specific data's protection level |
| SR-0289 | system_requirement | approved | Caching mechanisms are configured to only cache responses which have the expected content type for that resource and do not contain sensitive, dynamic content |
| SR-0290 | system_requirement | approved | The application only returns the minimum required sensitive data for the application's functionality |
| SR-0291 | system_requirement | approved | Sensitive information is subject to data retention classification, ensuring that outdated or unnecessary data is deleted automatically, on a defined schedule, or as the situation requires |
| SR-0292 | system_requirement | approved | Sensitive information is removed from the metadata of user-submitted files unless storage is consented to by the user |
| SR-0293 | system_requirement | approved | Authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated |
| SR-0294 | system_requirement | approved | The application sets sufficient anti-caching HTTP response header fields (i.e., Cache-Control: no-store) so that sensitive data is not cached in browsers |
| SR-0295 | system_requirement | approved | Data stored in browser storage (such as localStorage, sessionStorage, IndexedDB, or cookies) does not contain sensitive data, with the exception of session tokens |
<!-- tl:end -->

## V15 Secure Coding and Architecture

<!-- tl:item UR-0015 -->
**UR-0015 — V15 Secure Coding and Architecture** — `user_requirement`, status `approved`

> Verification requirements for Secure Coding and Architecture (V15).

*Derives from:* INT-0001

**source_ref**: V15
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V15.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0296 | system_requirement | approved | Application documentation defines risk based remediation time frames for 3rd party component versions with vulnerabilities and for updating libraries in general, to minimize the risk from these components |
| SR-0297 | system_requirement | approved | An inventory catalog, such as software bill of materials (SBOM), is maintained of all third-party libraries in use, including verifying that components come from pre-defined, trusted, and continually maintained repositories |
| SR-0298 | system_requirement | approved | The application documentation identifies functionality which is time-consuming or resource-demanding |
| SR-0299 | system_requirement | approved | Application documentation highlights third-party libraries which are considered to be "risky components" |
| SR-0300 | system_requirement | approved | Application documentation highlights parts of the application where "dangerous functionality" is being used |
| SR-0301 | system_requirement | approved | The application only contains components which have not breached the documented update and remediation time frames |
| SR-0302 | system_requirement | approved | The application has implemented defenses against loss of availability due to functionality which is time-consuming or resource-demanding, based on the documented security decisions and strategies for this |
| SR-0303 | system_requirement | approved | The production environment only includes functionality that is required for the application to function, and does not expose extraneous functionality such as test code, sample snippets, and development functionality |
| SR-0304 | system_requirement | approved | Third-party components and all of their transitive dependencies are included from the expected repository, whether internally owned or an external source, and that there is no risk of a dependency confusion attack |
| SR-0305 | system_requirement | approved | The application implements additional protections around parts of the application which are documented as containing "dangerous functionality" or using third-party libraries considered to be "risky components" |
| SR-0306 | system_requirement | approved | The application only returns the required subset of fields from a data object |
| SR-0307 | system_requirement | approved | Where the application backend makes calls to external URLs, it is configured to not follow redirects unless it is intended functionality |
| SR-0308 | system_requirement | approved | The application has countermeasures to protect against mass assignment attacks by limiting allowed fields per controller and action, e.g., it is not possible to insert or update a field value when it was not intended to be part of that action |
| SR-0309 | system_requirement | approved | All proxying and middleware components transfer the user's original IP address correctly using trusted data fields that cannot be manipulated by the end user, and the application and web server use this correct value for logging and security decisions such as rate limiting, taking into account that even the original IP address may not be reliable due to dynamic IPs, VPNs, or corporate firewalls |
| SR-0310 | system_requirement | approved | The application explicitly ensures that variables are of the correct type and performs strict equality and comparator operations |
| SR-0311 | system_requirement | approved | JavaScript code is written in a way that prevents prototype pollution, for example, by using Set() or Map() instead of object literals |
| SR-0312 | system_requirement | approved | The application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (query string, body parameters, cookies, or header fields) |
| SR-0313 | system_requirement | approved | Shared objects in multi-threaded code (such as caches, files, or in-memory objects accessed by multiple threads) are accessed safely by using thread-safe types and synchronization mechanisms like locks or semaphores to avoid race conditions and data corruption |
| SR-0314 | system_requirement | approved | Checks on a resource's state, such as its existence or permissions, and the actions that depend on them are performed as a single atomic operation to prevent time-of-check to time-of-use (TOCTOU) race conditions |
| SR-0315 | system_requirement | approved | Locks are used consistently to avoid threads getting stuck, whether by waiting on each other or retrying endlessly, and that locking logic stays within the code responsible for managing the resource to ensure locks cannot be inadvertently or maliciously modified by external classes or code |
| SR-0316 | system_requirement | approved | Resource allocation policies prevent thread starvation by ensuring fair access to resources, such as by leveraging thread pools, allowing lower-priority threads to proceed within a reasonable timeframe |
<!-- tl:end -->

## V16 Security Logging and Error Handling

<!-- tl:item UR-0016 -->
**UR-0016 — V16 Security Logging and Error Handling** — `user_requirement`, status `approved`

> Verification requirements for Security Logging and Error Handling (V16).

*Derives from:* INT-0001

**source_ref**: V16
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V16.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0317 | system_requirement | approved | An inventory exists documenting the logging performed at each layer of the application's technology stack, what events are being logged, log formats, where that logging is stored, how it is used, how access to it is controlled, and for how long logs are kept |
| SR-0318 | system_requirement | approved | Each log entry includes necessary metadata (such as when, where, who, what) that would allow for a detailed investigation of the timeline when an event happens |
| SR-0319 | system_requirement | approved | Time sources for all logging components are synchronized, and that timestamps in security event metadata use UTC or include an explicit time zone offset |
| SR-0320 | system_requirement | approved | The application only stores or broadcasts logs to the files and services that are documented in the log inventory |
| SR-0321 | system_requirement | approved | Logs can be read and correlated by the log processor that is in use, preferably by using a common logging format |
| SR-0322 | system_requirement | approved | When logging sensitive data, the application enforces logging based on the data's protection level |
| SR-0323 | system_requirement | approved | All authentication operations are logged, including successful and unsuccessful attempts |
| SR-0324 | system_requirement | approved | Failed authorization attempts are logged |
| SR-0325 | system_requirement | approved | The application logs the security events that are defined in the documentation and also logs attempts to bypass the security controls, such as input validation, business logic, and anti-automation |
| SR-0326 | system_requirement | approved | The application logs unexpected errors and security control failures such as backend TLS failures |
| SR-0327 | system_requirement | approved | All logging components appropriately encode data to prevent log injection |
| SR-0328 | system_requirement | approved | Logs are protected from unauthorized access and cannot be modified |
| SR-0329 | system_requirement | approved | Logs are securely transmitted to a logically separate system for analysis, detection, alerting, and escalation |
| SR-0330 | system_requirement | approved | A generic message is returned to the consumer when an unexpected or security-sensitive error occurs, ensuring no exposure of sensitive internal system data such as stack traces, queries, secret keys, and tokens |
| SR-0331 | system_requirement | approved | The application continues to operate securely when external resource access fails, for example, by using patterns such as circuit breakers or graceful degradation |
| SR-0332 | system_requirement | approved | The application fails gracefully and securely, including when an exception occurs, preventing fail-open conditions such as processing a transaction despite errors resulting from validation logic |
| SR-0333 | system_requirement | approved | A "last resort" error handler is defined which will catch all unhandled exceptions |
<!-- tl:end -->

## V17 WebRTC

<!-- tl:item UR-0017 -->
**UR-0017 — V17 WebRTC** — `user_requirement`, status `approved`

> Verification requirements for WebRTC (V17).

*Derives from:* INT-0001

**source_ref**: V17
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V17.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0334 | system_requirement | approved | The Traversal Using Relays around NAT (TURN) service only allows access to IP addresses that are not reserved for special purposes (e.g., internal networks, broadcast, loopback) |
| SR-0335 | system_requirement | approved | The Traversal Using Relays around NAT (TURN) service is not susceptible to resource exhaustion when legitimate users attempt to open a large number of ports on the TURN server |
| SR-0336 | system_requirement | approved | The key for the Datagram Transport Layer Security (DTLS) certificate is managed and protected based on the documented policy for management of cryptographic keys |
| SR-0337 | system_requirement | approved | The media server is configured to use and support approved Datagram Transport Layer Security (DTLS) cipher suites and a secure protection profile for the DTLS Extension for establishing keys for the Secure Real-time Transport Protocol (DTLS-SRTP) |
| SR-0338 | system_requirement | approved | Secure Real-time Transport Protocol (SRTP) authentication is checked at the media server to prevent Real-time Transport Protocol (RTP) injection attacks from leading to either a Denial of Service condition or audio or video media insertion into media streams |
| SR-0339 | system_requirement | approved | The media server is able to continue processing incoming media traffic when encountering malformed Secure Real-time Transport Protocol (SRTP) packets |
| SR-0340 | system_requirement | approved | The media server is able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users |
| SR-0341 | system_requirement | approved | The media server is not susceptible to the "ClientHello" Race Condition vulnerability in Datagram Transport Layer Security (DTLS) by checking if the media server is publicly known to be vulnerable or by performing the race condition test |
| SR-0342 | system_requirement | approved | Any audio or video recording mechanisms associated with the media server are able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users |
| SR-0343 | system_requirement | approved | The Datagram Transport Layer Security (DTLS) certificate is checked against the Session Description Protocol (SDP) fingerprint attribute, terminating the media stream if the check fails, to ensure the authenticity of the media stream |
| SR-0344 | system_requirement | approved | The signaling server is able to continue processing legitimate incoming signaling messages during a flood attack |
| SR-0345 | system_requirement | approved | The signaling server is able to continue processing legitimate signaling messages when encountering malformed signaling message that could cause a denial of service condition |
<!-- tl:end -->

