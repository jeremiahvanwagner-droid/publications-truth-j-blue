# Publications Truth J Blue

Static publications website for Truth J Blue and Jeremiah Van Wagner.

## Live Framework
- Auto-deploy to GitHub Pages from `main` via `.github/workflows/deploy-pages.yml`.
- CI validation via `.github/workflows/validate-site.yml`.
- Custom domain mapped with `CNAME` (`pub.jeremiahvanwagner.com`).

## Required GitHub Setting (one-time)
1. Open repository settings.
2. Go to **Pages**.
3. Set **Source** to **GitHub Actions**.

## Required DNS (for `pub.jeremiahvanwagner.com`)
- Create a `CNAME` record:
  - Host: `pub`
  - Value: `jeremiahvanwagner-droid.github.io`

## Site Entry Points
- `/` -> `index.html`
- `/publications.html`
- `/books.html`
- `/programs.html`
- `/sitemap.xml`

## Release
Any push to `main` triggers validation + deploy.

<!-- redeploy trigger 2026-02-17 22:50:44 UTC -->
