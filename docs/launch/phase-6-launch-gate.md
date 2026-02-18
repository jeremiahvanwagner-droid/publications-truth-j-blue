# Phase 6 Launch Gate

## Purpose
Phase 6 defines the go-live acceptance gate and handover process for `https://pub.jeremiahvanwagner.com`.

Launch is approved only when all technical and SEO acceptance checks pass.

## Automated Gate Commands
Production domain gate:

```bash
npm run launch:gate
```

Pre-cutover content gate (validates production canonical contract while fetching from GitHub Pages URL):

```bash
npm run launch:gate:github
```

Output report paths:
- `docs/launch/reports/latest-launch-gate.md`
- `docs/launch/reports/github-pages-audit.md`

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
1. If production gate fails due TLS/domain mapping, run `docs/launch/custom-domain-repair.md`.
2. Submit `https://pub.jeremiahvanwagner.com/sitemap.xml` in Google Search Console.
3. Submit the same sitemap in Bing Webmaster Tools.
4. Capture baseline crawl/index/query metrics in `docs/launch/baseline-metrics.md`.
5. Confirm v1 freeze status in `docs/releases/v1-freeze.md`.
6. Track deferred analytics/lead operations work in `docs/backlog/v1.1.md`.
