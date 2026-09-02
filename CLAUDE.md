# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-page web tribute to Enrique "Gato" Piedfort — waterpolo player, coach and dirigente, lifelong figure of **Club Gimnasia y Esgrima de Rosario** and the **Argentine Seleccionado Nacional** — plus a campaign to name **Rosario's** new municipal pool after him. Plain static HTML/CSS/JS, no build step. Bootstrap 5.3 loads from a CDN in `index.html`; `css/custom.css` is the site's own "waterline" design system layered on top.

Deliberate choices: no death date anywhere — the dates read `1945 – ∞`. The nickname is written with straight/curly double quotes ("Gato"), not guillemets.

## Structure

- `index.html` — most of the copy lives here directly. Spanish (voseo); `[bracketed]` spans and `.ph` class mark facts still to be filled in. The hero splits into two columns (copy 7 / photo 5); the photo is a `<figure class="hero-portrait">` with `img/gato_profile.*` and a caption.
- `data.json` — the **only** externalised content: the `testimonios`, `galeria` and `trayectoria` lists, plus a `flags` object. `js/app.js` fetches it on load and renders those three sections. A failed fetch (e.g. opening via `file://`) leaves them empty — preview through a local server.
- `data.json` → `flags` — feature switches. `flags.propuesta` (default `false`) gates the "La propuesta" section (`#propuesta`) and its nav button. Both carry `hidden` in the HTML and fail closed; `app.js`'s `applyFlags()` reveals them only when the flag is `true`. Flip it to `true` once the pool-naming proposal has approval.
- `js/app.js` — fetch + render of the three lists, `applyFlags()`, plus the gallery lightbox (Bootstrap modal), scroll reveals, nav behaviour and share buttons.
- `img/*.svg` — placeholder stand-ins to be replaced with real photos (`g*` = gallery, `t*` = trayectoria; keep the filenames or update `data.json`).
- `img/gato_profile.{webp,jpg}` — hero photo, served via `<picture>` (WebP with JPEG fallback), `fetchpriority="high"`. `img/gato_profile.png` is the kept original master (~1.6 MB, not referenced by the page) and the source for `img/og.jpg`. Re-run the WebP/JPEG export from the PNG if the photo changes.
- `img/gato_profile_vintage.jpg` — portrait shown in the "Su historia" section.
- `img/og.jpg` — the social-card image (1200×630), composed from `img/gato_profile.png`. Referenced by the `og:image` / `twitter:image` tags with explicit width/height. Regenerate it if that source photo or the name/dates change.
- `favicon.svg`, `robots.txt`, `sitemap.xml`, `.nojekyll` — SEO/serving basics at the repo root. Update `sitemap.xml` `lastmod` on meaningful content changes; the `<script type="application/ld+json">` block in `index.html` carries the `Person` + `WebSite` structured data (no `deathDate`).
- `assets/qr/` — QR code (vector + raster) pointing at the live URL, for a printed banner. `qr-marca.svg` is also shown in the on-page "Compartir" section. `LEER.md` there explains which file to send to print. Regenerate with `segno` if the URL changes.
- The "Apoyar la propuesta" / "Descargar carta" buttons are **placeholders** — a separate verified-voting app will own real signatures. Do not wire a real form into this repo.

## Deploy

GitHub Pages serves the repo root from `main`. Any push to `main` publishes the live site at `enriquepiedfort.waterpoloargentina.com`. There is no staging environment; test locally by opening `index.html` in a browser.

## Formatting

`npm run format` (Prettier) formats HTML/CSS/JS/MD. Run it before committing. Requires `npm install` first (Node is not preinstalled on this machine — `sudo snap install node --classic`).

## Gotchas

- `CNAME` pins the custom domain. Do not delete or edit it — removing it breaks the domain mapping on the next deploy.
- `css/custom.css` colours come from `:root` tokens. Each palette colour has a hex token (`--deep`) and an RGB-triplet token (`--deep-rgb`) for `rgba(var(--deep-rgb), α)` — use those, don't inline colour literals. Shared "sunk card" border/shadow: `--card-border` / `--card-shadow`.
- Preview with `python3 -m http.server` (Node/npm are not installed on this machine; `file://` also works but a server matches production).
