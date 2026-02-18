# Truth J Blue Publications Plan (Finalized)

Last updated: February 18, 2026
Owner: Truth J Blue / Jeremiah Van Wagner
Execution model: Static HTML/CSS, GitHub Pages, canonical domain `https://pub.jeremiahvanwagner.com`

## 1. Objective
Deliver a publication-grade web presence that establishes Truth J Blue as a leader in consciousness and self-mastery while remaining crawlable, indexable, and operationally simple.

## 2. Final Information Architecture
- Home: `/`
- Publications hub: `/publications.html`
- Books catalog: `/books.html`
- Programs ladder: `/programs.html`
- About voice page: `/about-jeremiah.html`
- Manifesto doctrine page: `/manifesto.html`
- Philosophy page: `/philosophy.html`
- Support/legal: `/contact.html`, `/privacy.html`, `/terms.html`, `/404.html`
- Crawl endpoints: `/sitemap.xml`, `/robots.txt`, `/sitemap.html`

## 3. Phase Completion Status
1. Phase 1 (Publish boundary hardening): Complete
2. Phase 2 (Design and UX polish): Complete
3. Phase 3 (Conversion policy and legal/support): Complete
4. Phase 4 (SEO/crawler completion): Complete
5. Phase 5 (Deployment and DNS cutover): In progress (DNS cutover pending)
6. Phase 6 (Launch gate and handover ops): Complete

## 4. Delivered Build Components
- Production deploy root isolated to `site/`.
- Source content isolated to `content/` and `content/internal/`.
- CI validation for metadata, schema, sitemap, robots, links, and policy checks.
- Full static page system with consistent navigation/footer patterns.
- Program page policy implemented (program-page links only, no direct checkout links).
- Legal and contact pages deployed.
- Long-form manifesto source converted to markdown:
  - `content/truth-j-blue-manifesto.md`
- Manifesto page rewritten to reflect doctrinal framework and practical application.

## 5. Launch Blocker (Current)
Custom domain DNS is not consistently routed to GitHub Pages edge. This keeps production gate in `FAIL` even when site files are healthy.

Action required in DNS provider:
1. Remove `A` and `AAAA` records for host `pub`.
2. Add `CNAME` only:
- Host: `pub`
- Value: `jeremiahvanwagner-droid.github.io`
3. Set TTL to `300` during cutover.

Action required in GitHub:
1. Repository Settings -> Pages -> Source: `GitHub Actions`.
2. Custom domain: `pub.jeremiahvanwagner.com`.
3. Enable HTTPS enforcement after certificate issuance.

## 6. Completion Gate
Launch is considered complete only when:
1. `npm run launch:gate` returns `PASS`.
2. `docs/launch/reports/latest-launch-gate.md` shows all checks passing.
3. Custom domain serves all canonical URLs over HTTPS.

## 7. Post-Launch Operations
1. Submit `https://pub.jeremiahvanwagner.com/sitemap.xml` to Google Search Console.
2. Submit same sitemap to Bing Webmaster Tools.
3. Capture baseline metrics in `docs/launch/baseline-metrics.md`.
4. Move deferred improvements to v1.1 from `docs/backlog/v1.1.md`.

## 8. v1.1 Deferred Scope
- Analytics instrumentation and conversion event model.
- Lead operations routing and response workflow.
- CTR optimization and expansion content.
