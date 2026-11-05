# Vulnerability Map: Areas and Specific Issues to Research

A starting map of the main security weakness areas. No list can be literally complete (CWE alone has hundreds of entries), but each area below covers topics worth searching individually.

| Area | Specific issues to search | Best place to learn |
|---|---|---|
| Access control | IDOR/BOLA, privilege escalation, forced browsing, path traversal, CORS misconfiguration | PortSwigger, OWASP WSTG |
| Injection | SQLi, NoSQLi, OS command injection, LDAP injection, SSTI, XXE, header/CRLF injection, log injection | PortSwigger |
| Client-side | XSS (stored, reflected, DOM), CSRF, clickjacking, open redirect, postMessage flaws, prototype pollution | PortSwigger |
| Server-side request and parsing | SSRF, HTTP request smuggling, host header attacks, web cache poisoning, cache deception | PortSwigger |
| Authentication and sessions | Credential stuffing, weak password reset, session fixation, JWT flaws, OAuth/OIDC flaws, MFA bypass | PortSwigger, OWASP Cheat Sheets |
| Business logic | Race conditions (TOCTOU), price manipulation, workflow bypass, missing rate limits | PortSwigger, WSTG |
| Cryptography and data exposure | Weak algorithms, hardcoded keys, bad randomness, no TLS, secrets in URLs or logs | OWASP Cheat Sheets, CWE |
| Integrity and deserialization | Insecure deserialization, unsigned updates, tampered CI/CD pipelines | PortSwigger, CWE |
| File handling | Unrestricted upload, zip slip, path traversal | WSTG |
| Supply chain | Vulnerable dependencies, typosquatting, dependency confusion, leaked secrets in repos | OWASP Top 10 A03, OWASP Dependency-Check |
| Configuration | Default credentials, debug mode on, exposed admin panels, open cloud storage, missing security headers, verbose errors | WSTG, CIS Benchmarks |
| Logging and monitoring | No audit logs, no alerting, logs that can be tampered with | OWASP Top 10 A09 |
| APIs | Mass assignment, broken function-level authorization, excessive data exposure, unrestricted resource consumption, GraphQL abuse | OWASP API Security Top 10 |
| Denial of service | ReDoS, algorithmic complexity attacks, resource exhaustion | CWE |
| Cloud and containers | IAM misconfiguration, exposed metadata service, container escape, secrets baked into images | CIS Benchmarks, cloud provider docs |
| Mobile | Insecure local storage, missing certificate pinning, exported components | OWASP MASVS and Mobile Top 10 |
| AI/LLM apps | Prompt injection, insecure output handling, data leakage, excessive agency | OWASP Top 10 for LLM Applications |
| Memory safety (non-web) | Buffer overflow, use-after-free, integer overflow | CWE Top 25 |
| Design and process | Missing threat modeling, insecure design, social engineering, phishing | OWASP Top 10 A06, OWASP Threat Dragon |

## Resources

- **OWASP Top 10:2025**: https://owasp.org/Top10/2025/
- **CWE (full weakness catalog)**: https://cwe.mitre.org
- **CWE Top 25**: yearly list of most dangerous weaknesses (MITRE)
- **CAPEC**: catalog of attack patterns (attacker's view)
- **OWASP ASVS**: detailed security requirements checklist
- **OWASP WSTG**: step-by-step web testing guide
- **OWASP Cheat Sheet Series**: short practical guides per topic
- **PortSwigger Web Security Academy**: free explanations and hands-on labs
- **OWASP Juice Shop / WebGoat**: intentionally vulnerable apps to practice on

## How to avoid gaps

1. Go through the table one row at a time and search each specific term.
2. Look up unfamiliar terms in CWE.
3. When done, skim ASVS and compare its chapters to the rows above. Anything it covers that the table doesn't is a gap.