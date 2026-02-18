# Phase 6 Launch Gate

## Purpose
Phase 6 defines the go-live acceptance gate and handover process for `https://pub.jeremiahvanwagner.com`.

Launch is approved only when all technical and SEO acceptance checks pass.

## Automated Gate Command
Run after each production deploy:

```bash
python scripts/launch_gate.py --base-url https://pub.jeremiahvanwagner.com
```

Output report path:
- `docs/launch/reports/latest-launch-gate.md`

Gate status rules:
- `PASS`: all checks pass.
- `FAIL`: one or more checks fail.

## Required Acceptance Criteria
1. GitHub Actions succeeded on `main`:
- `Validate Static Site`
- `Deploy Static Site to GitHub Pages`
2. `latest-launch-gate.md` is `PASS`.
3. `https://pub.jeremiahvanwagner.com/` serves the expected homepage over valid HTTPS.
4. Core pages return `200` and `/404-test` shows custom 404 behavior.
5. `robots.txt` and `sitemap.xml` are valid and aligned to canonical URLs.
6. Metadata parity and JSON-LD validity pass on live pages.
7. Program page contains program-page links only (no direct checkout links).

## Manual Handover Tasks
1. Submit `https://pub.jeremiahvanwagner.com/sitemap.xml` in Google Search Console.
2. Submit the same sitemap in Bing Webmaster Tools.
3. Capture baseline crawl/index/query metrics in `docs/launch/baseline-metrics.md`.
4. Confirm v1 freeze status in `docs/releases/v1-freeze.md`.
5. Track deferred analytics/lead operations work in `docs/backlog/v1.1.md`.
