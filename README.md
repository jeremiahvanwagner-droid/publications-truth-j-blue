# Publications Truth J Blue

Static publication website for Truth J Blue and Jeremiah Van Wagner.

## Production Contract
- Canonical domain: `https://pub.jeremiahvanwagner.com`
- Hosting: GitHub Pages (GitHub Actions deploy)
- Deploy root: `site/`

## Repository Layout
- `site/`: Public web artifact only (HTML, CSS, crawl files, assets).
- `content/`: Source material and product content (not deployed).
- `content/internal/`: Planning and internal docs (not deployed).
- `.github/workflows/`: CI validation and Pages deploy.

## Public Files Policy
Only files inside `site/` are published. Source docs must remain outside `site/`.

Restricted from publish artifact:
- `*.md` source and planning docs
- internal notes and non-web authoring files

## CI/CD
- `.github/workflows/validate-site.yml`
  - validates `site/` structure
  - checks sitemap/robots
  - enforces metadata parity and single `h1`
  - parses JSON-LD
  - checks local links/assets
  - blocks legacy Word export artifacts
- `.github/workflows/deploy-pages.yml`
  - uploads only `site/` to GitHub Pages

## Required GitHub Setting (one-time)
1. Open repository **Settings**.
2. Open **Pages**.
3. Set **Source** to **GitHub Actions**.

## DNS Cutover (`pub.jeremiahvanwagner.com`)
At your DNS provider:
1. Remove existing `A` and `AAAA` records for host `pub`.
2. Add `CNAME`:
   - Host: `pub`
   - Value: `jeremiahvanwagner-droid.github.io`
3. Set TTL to `300` during cutover.

Repository domain file:
- `site/CNAME` must remain `pub.jeremiahvanwagner.com`

## Release Flow
Any push to `main`:
1. runs `Validate Static Site`
2. deploys `site/` via `Deploy Static Site to GitHub Pages`

## Production URLs
- `/`
- `/publications.html`
- `/books.html`
- `/programs.html`
- `/about-jeremiah.html`
- `/manifesto.html`
- `/philosophy.html`
- `/sitemap.html`
- `/contact.html`
- `/privacy.html`
- `/terms.html`
- `/sitemap.xml`
- `/robots.txt`


## Framework Workspace (Optional)
A Next.js + Tailwind workspace is installed for future migration work, without changing current static deploy behavior.

Commands:
- `npm run dev`
- `npm run build`
- `npm run start`

Important:
- Production GitHub Pages deployment still publishes only `site/`.
- Framework files (`app/`, `next.config.mjs`) are currently non-deploying scaffolding.

