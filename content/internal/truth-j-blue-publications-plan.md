# Truth J Blue Publications Plan

Last prepared: February 18, 2026
Source content reviewed in this folder: 10 books, 8 products, existing About/Manifesto/Philosophy/Sitemap/Robots files

## 1. Goal
Create a publications presence that positions Truth J Blue (Jeremiah Van Wagner) as a recognized voice in consciousness, spiritual alignment, and self-mastery while maximizing crawlability, indexation, and long-term topical authority.

## 2. What Is Already Available
- `truth-j-blue-books.md`: 10 book listings with topic, URL, ISBN, SKU, price, keyword set, and descriptions.
- `truth-j-blue-products.md`: 8 offers with URL, payment link, price, and SEO metadata.
- Voice and doctrine pages: `about-jeremiah.html`, `manifesto.html`, `philosophy.html`.

## 3. Current State Risks To Fix First
1. Multiple HTML files are Word-export wrappers with escaped HTML (not clean semantic pages):
   - `about-jeremiah.html:5`, `about.html:5`, `manifesto.html:5`, `philosophy.html:5`, `sitemap.html:5`
   - Escaped doctype text appears in body content, not as real HTML (`about-jeremiah.html:42`, etc.).
2. `index.html` is effectively empty (`index.html:39`).
3. XML sitemap files are Word package XML, not valid sitemap XML for crawlers:
   - `index.xml.xml`, `manifesto-sitemap.xml:2`
4. `robots.txt` points to `manifesto-sitemap.xml` (`robots.txt:4`), which should be replaced with a valid sitemap endpoint.
5. Canonical strategy has overlap/duplication risk (`about.html` and `about-jeremiah.html` both point to `/about.html`).

## 4. Architecture Decision: 1 Page vs 3 Pages

### Option A: One Long Page (`/publications`)
Best when speed of launch is priority and maintenance bandwidth is limited.
- Strong single authority URL.
- Simple crawl path and straightforward internal linking.
- Higher risk of keyword dilution (books + offers + manifesto voice all competing on one URL intent).

### Option B: Three-Page System (Recommended)
Best for authority building and clearer search intent.
1. `/publications` (pillar page)
   - Brand thesis, Jeremiah voice, publication framework, featured works, clear routing.
2. `/books` (catalog authority)
   - Full 10-book collection with topic clusters, ISBN metadata, and excerpts.
3. `/programs` (transformation offer ladder)
   - Full 8-offer progression from entry to premium engagement.

Why this is recommended:
- Cleaner intent per URL.
- Better title/description targeting.
- Stronger internal topical cluster and breadcrumbs.
- Easier to scale with future books and courses.

## 5. Proposed Information Architecture (Recommended)
- Home: `/` (brand gateway)
- Publications hub: `/publications`
- Books: `/books`
- Programs: `/programs`
- About Jeremiah: `/about-jeremiah`
- Manifesto: `/manifesto`
- Philosophy: `/philosophy`

## 6. Content Model

### Books (from existing markdown)
Use each book as an indexable card + optional detail page later.
Required fields:
- Title
- Topic
- Short description
- ISBN
- Price
- Store URL
- Primary keyword cluster

### Programs (from existing markdown)
Use each offer as a journey-stage card.
Suggested stages:
- Entry: Inner Alignment Audit, Purpose Activation Toolkit
- Core: Scorecard Deep-Dive Workshop, Ascension Intensive
- Advanced: Beyond the Veil Mentorship, VIP Mastermind
- Executive: Private Coaching, Strategic Partnership

### Voice Layer (Jeremiah authority signals)
Cross-link every page to:
- Personal mission statement
- Methodology/pillars
- Manifesto and philosophy
- Real-world outcomes/testimonials (as available)

## 7. SEO and Crawler Blueprint

### Technical foundation
- Replace Word-export wrappers with valid semantic HTML5.
- Use UTF-8 encoding across all files.
- One canonical per indexable page, self-referencing.
- Unique title + meta description per page.
- Valid XML sitemap (`/sitemap.xml`) listing all canonical URLs.
- Update `robots.txt` to reference the new sitemap URL.

### On-page SEO
- One clear `H1` per page.
- Descriptive `H2` hierarchy by theme and user intent.
- Crawlable HTML links (`<a href="...">`) for all navigation and cards.
- Intro copy that states purpose, audience, and transformation outcome.

### Structured data (JSON-LD)
- `Organization` on home/about/publications hub.
- `Person` + `ProfilePage` on about page for Jeremiah entity clarity.
- `Book` objects on books page for each title.
- `Product` objects on programs page for offers.
- `BreadcrumbList` on all major pages.

### Discovery and indexing
- Submit sitemap in Google Search Console and Bing Webmaster Tools.
- Optional acceleration: enable IndexNow after launch.

## 8. Page-Level Outline (3-page version)

### `/publications`
- Hero: Truth J Blue Publications by Jeremiah Van Wagner
- Positioning statement (consciousness + self-mastery + divine alignment)
- Three pillar blocks:
  - Books for inner transformation
  - Programs for applied mastery
  - Doctrine (manifesto/philosophy)
- Featured works (3 books, 3 programs)
- CTA row to `/books`, `/programs`, `/about-jeremiah`

### `/books`
- Intro: purpose of the collection
- Filter anchors by topic:
  - Abundance and prosperity
  - Intention and manifestation
  - Emotional and mental mastery
  - Leadership and communication
  - Faith and spiritual responsibility
- 10 book cards with standardized metadata
- CTA to programs

### `/programs`
- Intro: transformation pathway
- Offer ladder by stage (entry to executive)
- 8 offer cards with outcomes, price, and CTA
- Trust section (approach, fit criteria, FAQs)
- CTA to book catalog and contact/application flow

## 9. 30-60-90 Day Rollout

### Days 1-14 (Build and launch)
- Rebuild files in clean HTML.
- Publish the 3-page architecture.
- Deploy metadata, schema, sitemap, robots.
- Submit for indexing.

### Days 15-45 (Authority strengthening)
- Add 3 to 6 supporting articles tied to core themes.
- Add testimonial/outcome blocks where possible.
- Improve internal links from manifesto/philosophy/about to books/programs.

### Days 46-90 (Optimization)
- Review Search Console coverage, queries, and CTR.
- Expand high-impression pages with richer sections.
- Add detail pages for top-performing books/programs if needed.

## 10. Success Metrics
- All core pages indexed and canonicalized correctly.
- Valid rich-result eligible structured data on books/program pages.
- Growth in impressions/clicks for branded and topical queries.
- Improved engagement on books/programs pages (scroll depth and outbound CTR).

## 11. Immediate Next Build Order
1. Fix technical foundation (HTML cleanup, sitemap, robots, canonicals).
2. Launch `/publications`, `/books`, `/programs`.
3. Apply schema + internal linking.
4. Submit and monitor indexing.

