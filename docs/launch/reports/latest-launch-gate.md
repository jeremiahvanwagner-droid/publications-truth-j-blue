# Phase 6 Launch Gate Report

- Run (UTC): 2026-02-18 13:44:27Z
- Canonical Base URL: https://pub.jeremiahvanwagner.com
- Fetch Base URL: https://pub.jeremiahvanwagner.com
- Gate Status: FAIL
- Checks Passed: 3/19

| Status | Check | Detail |
| --- | --- | --- |
| FAIL | DNS contract | pub.jeremiahvanwagner.com resolves to non-GitHub IPs: 191.96.144.37, 195.35.60.38, 2a02:4780:1e:4990:2f46:9529:a1ed:232e, 2a02:4780:21:a680:1cc0:fc07:96d5:f900 |
| PASS | Core URL / returns 200 | HTTP 200 |
| FAIL | Core URL /publications.html returns 200 | HTTP 404 |
| FAIL | Core URL /books.html returns 200 | HTTP 404 |
| FAIL | Core URL /programs.html returns 200 | HTTP 404 |
| FAIL | Core URL /about-jeremiah.html returns 200 | HTTP 404 |
| FAIL | Core URL /manifesto.html returns 200 | HTTP 404 |
| FAIL | Core URL /philosophy.html returns 200 | HTTP 404 |
| FAIL | Core URL /sitemap.html returns 200 | HTTP 404 |
| FAIL | Core URL /contact.html returns 200 | HTTP 404 |
| FAIL | Core URL /privacy.html returns 200 | HTTP 404 |
| FAIL | Core URL /terms.html returns 200 | HTTP 404 |
| FAIL | about.html alias behavior | Unexpected HTTP 404 |
| FAIL | robots.txt reachable | HTTP 404 |
| FAIL | sitemap.xml reachable | HTTP 404 |
| PASS | Custom 404 behavior | HTTP 404 |
| FAIL | Live metadata parity | / missing canonical; / missing og:title; / missing og:description; / missing og:image; / missing twitter:card; / missing twitter:title; / missing twitter:description; / missing twitter:image; / missing canonical href |
| PASS | Live JSON-LD validity | all JSON-LD blocks parsed |
| FAIL | Program link policy | /programs.html was not available for policy checks |
