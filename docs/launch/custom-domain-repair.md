# Custom Domain Repair Checklist

This checklist resolves the current production blocker where `pub.jeremiahvanwagner.com` serves GitHub 404 with a certificate mismatch.

## Current Evidence (2026-02-18 UTC)
- DNS is pointed correctly:
  - `pub.jeremiahvanwagner.com CNAME jeremiahvanwagner-droid.github.io`
- HTTPS on custom domain fails hostname validation.
- Insecure fetch returns GitHub default 404 page (`There isn't a GitHub Pages site here.`).
- GitHub Pages URL content is healthy and launch gate passes when fetched directly.

## Required Repairs in GitHub
1. Open repository `publications-truth-j-blue` -> `Settings` -> `Pages`.
2. Confirm `Build and deployment` source is `GitHub Actions`.
3. In `Custom domain`, explicitly set:
   - `pub.jeremiahvanwagner.com`
4. Save and wait for GitHub domain verification to complete.
5. Enable `Enforce HTTPS` after certificate is issued.

## Required Repairs in DNS Provider
1. Keep only one record for host `pub`:
   - Type: `CNAME`
   - Value: `jeremiahvanwagner-droid.github.io`
2. Remove any conflicting `A`/`AAAA` records on host `pub`.
3. TTL target during cutover: `300` (currently observed around `915`).

## Verification Sequence
1. Run production gate:
   - `npm run launch:gate`
2. Expected outcome:
   - `docs/launch/reports/latest-launch-gate.md` shows `Gate Status: PASS`.
3. If still failing TLS, wait propagation and re-run every 15-30 minutes.
4. If TLS is fixed but content still 404, re-check GitHub Pages custom-domain ownership and assignment.
