# Redeploy Guide — pub.jeremiahvanwagner.com (Hostinger)

The publication site source was never lost. The deployed/hosting layer was removed; the
files in `site/` are intact and were enhanced (visual refresh + SEO + new social card).
This guide gets the enhanced site back live at `https://pub.jeremiahvanwagner.com`.

The site is a **static** site (plain HTML/CSS). It needs ordinary static hosting — no
Node, no build step on the server.

Deployable bundle: `pub-jeremiahvanwagner-site.zip` (contents of `site/` at the archive root).

---

## Option A — Host directly on Hostinger (simplest, matches your setup)

Use this if `pub.jeremiahvanwagner.com` should be served from Hostinger itself.

1. Hostinger hPanel → **Websites** → select the site/subdomain for `pub.jeremiahvanwagner.com`
   (create the subdomain under `jeremiahvanwagner.com` if it no longer exists).
2. Open **File Manager** and go to that site's document root
   (usually `public_html/` or `public_html/pub/`).
3. Delete the old/placeholder files (the current "Framework Workspace" page).
4. Upload `pub-jeremiahvanwagner-site.zip` and **Extract** it there, so `index.html`
   sits directly in the document root (not inside a `site/` subfolder).
5. Confirm DNS: hPanel → **Domains → DNS / Nameservers**. The `pub` host should resolve
   to this Hostinger site (A record to your Hostinger IP, or the subdomain mapping
   Hostinger created). Remove any stale record pointing `pub` elsewhere.
6. Enable **SSL** for the subdomain (hPanel → SSL) and force HTTPS.
7. Visit `https://pub.jeremiahvanwagner.com` — you should see the refreshed Truth J Blue
   home page (hero: "Truth J Blue as the Voice of Jeremiah Van Wagner").

Notes:
- `CNAME` and `.nojekyll` in the bundle are GitHub-Pages artifacts; harmless on Hostinger,
  safe to leave or delete.

## Option B — Automated deploys via GitHub Pages + Hostinger DNS

Use this if you want every push to `main` to auto-publish (the repo already has the workflow).

1. GitHub repo `jeremiahvanwagner-droid/publications-truth-j-blue` →
   **Settings → Pages → Source = GitHub Actions**, Custom domain = `pub.jeremiahvanwagner.com`.
2. In Hostinger DNS for `jeremiahvanwagner.com`, set host `pub`:
   - Remove existing `A`/`AAAA`/`CNAME` records for `pub`.
   - Add `CNAME`  →  host `pub`, value `jeremiahvanwagner-droid.github.io`, TTL 300.
3. Push this repo (with the enhanced `site/`). The `Deploy Static Site to GitHub Pages`
   workflow uploads only `site/`.
4. After the cert issues in GitHub Pages, enable **Enforce HTTPS**.

Pick **one** option — A and B both want to control the same `pub` DNS record, so don't run them at once.

---

## What changed in this enhancement pass
- `site/styles.css` — full visual refresh (Fraunces display type, gradient hero + headings,
  refined nav/cards/stats/footer, focus-visible a11y, smooth motion with reduced-motion support).
- `site/assets/og-default.svg` — upgraded social share card (same path, so CI contract holds).
- All pages — added `theme-color`, `author`, and font `preconnect` hints.
- Verified against every check in `.github/workflows/validate-site.yml` (all pass).
