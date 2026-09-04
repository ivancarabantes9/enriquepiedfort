# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-page web tribute to Enrique "Gato" Piedfort — waterpolo player, coach and dirigente, lifelong figure of **Club Gimnasia y Esgrima de Rosario** and the **Argentine Seleccionado Nacional**. Plain static HTML/CSS/JS, no build step. Bootstrap 5.3 loads from a CDN in `index.html`; `css/custom.css` is the site's own "waterline" design system layered on top.

There is no pool-naming "La propuesta" section anymore — it was removed (HTML, its `#propuesta`/nav-button markup, the `flags.propuesta` switch, `applyFlags()` in `js/app.js`, and the `.proposal-*`/`.btn-support` CSS) because the campaign wasn't ready to be public. If it needs to come back, it'll be reintroduced deliberately rather than un-hidden.

Deliberate choices: no death date anywhere — the dates read `1945 – ∞`. The nickname is written with straight/curly double quotes ("Gato"), not guillemets.

## Structure

- `index.html` — most of the copy lives here directly. Spanish (voseo); `[bracketed]` spans and `.ph` class mark facts still to be filled in. The hero splits into two columns (copy 7 / photo 5); the photo is a `<figure class="hero-portrait">` with `img/gato_profile.*` and a caption.
- `data.json` — the **only** externalised content: the `testimonios`, `galeria` and `trayectoria` lists. `js/app.js` fetches it on load and renders those three sections. A failed fetch (e.g. opening via `file://`) leaves them empty — preview through a local server.
- `js/app.js` — fetch + render of the three lists, the gallery lightbox (Bootstrap modal), scroll reveals, nav behaviour and share buttons.
- `img/g-*.jpg` — the gallery photos, listed in `data.json` → `galeria`. Optimised historical scans (~1400px, progressive JPEG). Two of them (`g-1972-*`, `g-1974-*`) are reused as the `img` of the matching `trayectoria` milestones. Milestones without a real photo simply have no `img`/`alt` key (text-only card) — don't reintroduce placeholder SVGs for them; add the key only once a real photo exists.
- `img/gato_profile.{webp,jpg}` — hero photo, served via `<picture>` (WebP with JPEG fallback), `fetchpriority="high"`. `img/gato_profile.png` is the kept original master (~1.6 MB, not referenced by the page) and the source for `img/og.jpg`. Re-run the WebP/JPEG export from the PNG if the photo changes.
- `img/gato_profile_vintage.jpg` — portrait shown in the "Su historia" section.
- `img/og.jpg` — the social-card image (1200×630), composed from `img/gato_profile.png`. Referenced by the `og:image` / `twitter:image` tags with explicit width/height. Regenerate it if that source photo or the name/dates change.
- `favicon.svg`, `robots.txt`, `sitemap.xml`, `.nojekyll` — SEO/serving basics at the repo root. Update `sitemap.xml` `lastmod` on meaningful content changes; the `<script type="application/ld+json">` block in `index.html` carries the `Person` + `WebSite` structured data (no `deathDate`).
- `assets/qr/` — QR code (vector + raster) pointing at the live URL, for a printed banner. `qr-marca.svg` is also shown in the on-page "Compartir" section. `LEER.md` there explains which file to send to print. Regenerate with `segno` if the URL changes.

## Deploy

GitHub Pages serves the repo root from `main`. Any push to `main` publishes the live site at `enriquepiedfort.waterpoloargentina.com`. There is no staging environment; test locally by opening `index.html` in a browser.

## Formatting

`npm run format` (Prettier) formats HTML/CSS/JS/MD. Run it before committing. Requires `npm install` first (Node is not preinstalled on this machine — `sudo snap install node --classic`).

## Gotchas

- `CNAME` pins the custom domain. Do not delete or edit it — removing it breaks the domain mapping on the next deploy.
- `css/custom.css` colours come from `:root` tokens. Each palette colour has a hex token (`--deep`) and an RGB-triplet token (`--deep-rgb`) for `rgba(var(--deep-rgb), α)` — use those, don't inline colour literals. Shared "sunk card" border/shadow: `--card-border` / `--card-shadow`.
- Preview with `python3 -m http.server` (Node/npm are not installed on this machine; `file://` also works but a server matches production).
