# Penetration Test — OWASP Juice Shop

**Project:** Penetration test on OWASP Juice Shop (local lab)  
**Purpose:** Practice and demonstrate web-app pen-testing skills; document findings and remediation.  
**Tools used:** Kali Linux tools (nmap, nikto, sqlmap), OWASP ZAP, Burp Suite, Docker.

## Folder contents
- `juice-shop-penetration-report.md` — Final pentest report (Markdown; can export to PDF).  
- `scans/` — raw tool outputs (nmap, nikto, zap).  
- `artifacts/` — screenshots, pcaps, exploit scripts.  
- `evidence-log.md` — step-by-step log of actions & timestamps.

## How to run the lab (quick)
1. Start Juice Shop with Docker:
   ```bash
   docker run --rm -p 3000:3000 bkimminich/juice-shop

