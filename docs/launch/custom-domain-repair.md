# Custom Domain Repair Checklist

This checklist resolves the production blocker where `pub.jeremiahvanwagner.com` serves non-publication content and returns 404 for publication paths.

## Current Evidence (2026-02-18 UTC)
- `npm run launch:gate` fails (`3/19`) and reports `DNS contract` failure.
- DNS for host `pub` resolves to non-GitHub addresses (see `docs/launch/reports/latest-launch-gate.md` for current values).
- Expected for GitHub Pages hosting: CNAME `pub -> jeremiahvanwagner-droid.github.io`.

## Required Repairs in DNS Provider (Client-Owned)
1. Delete all existing `A` and `AAAA` records for host `pub`.
2. Create one record:
- Type: `CNAME`
- Host: `pub`
- Value: `jeremiahvanwagner-droid.github.io`
3. Set TTL to `300` during cutover.
4. Save and wait for propagation.

## Required GitHub Pages Verification
1. Open repository `publications-truth-j-blue` -> `Settings` -> `Pages`.
2. Confirm `Build and deployment` source is `GitHub Actions`.
3. Confirm `Custom domain` is set to:
- `pub.jeremiahvanwagner.com`
4. Enable `Enforce HTTPS` once certificate is issued.

## Verification Sequence
1. Confirm DNS now resolves to GitHub Pages edge IPs.
2. Run production gate:
- `npm run launch:gate`
3. Expected outcome:
- `docs/launch/reports/latest-launch-gate.md` shows `Gate Status: PASS`.
4. If still failing, wait 15-30 minutes and re-run until propagation completes.
