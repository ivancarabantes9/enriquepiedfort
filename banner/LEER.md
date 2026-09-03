# Banner homenaje — Enrique "Gato" Piedfort

Banner vertical para impresión, **85 × 200 cm** (relación exacta del archivo).

Composición, de arriba hacia abajo: foto a sangre en la franja superior (se funde con el
fondo de agua), nombre completo con el degradado "waterline", `1945 – ∞`, la frase, y el
QR con su llamada. Sin dirección web ni pie de autoría.

## Archivos

| Archivo | Para qué |
|---|---|
| **`banner-gato-piedfort-85x200.svg`** | El maestro. Vectorial, a tamaño real (850 × 2000 mm). Se abre en **Adobe Illustrator** con *Archivo → Abrir*: entra como documento editable — cada texto sigue siendo texto, el QR es vectorial, la foto va embebida. |
| `banner-gato-piedfort-85x200-preview.png` | Vista previa de referencia (1275 × 3000 px). **No usar para imprimir** — las tipografías son sustitutas. |

### Cómo obtener un `.ai` nativo

No se puede generar un binario `.ai` sin Illustrator. El camino es:

1. Abrir el SVG en Illustrator.
2. Instalar/activar las tres tipografías (ver abajo). Illustrator avisa si faltan y las sustituye; el texto se mantiene editable.
3. *Archivo → Guardar como → Adobe Illustrator (`.ai`)*.

Para la gráfica, si piden PDF: *Archivo → Guardar como → PDF (imprenta)*, marcar sangrado y **convertir textos a contornos** (*Texto → Crear contornos*) antes de exportar si no quieren instalar las fuentes.

## Tipografías (las mismas del sitio, gratuitas)

- **Anton** — el nombre. <https://fonts.google.com/specimen/Anton>
- **Barlow Condensed** / **Barlow** — "HOMENAJE" y las fechas. <https://fonts.google.com/specimen/Barlow+Condensed>
- **Source Serif 4** (itálica) — la frase y el texto del QR. <https://fonts.google.com/specimen/Source+Serif+4>

Todas están también en Adobe Fonts (activación con un clic desde Illustrator).

## Colores (sistema "waterline" del sitio)

| | hex |
|---|---|
| Profundo (fondo) | `#04263A` → `#072F47` → `#021A29` (degradado vertical) |
| Turquesa | `#3FC1C9` |
| Azul pileta | `#0B6E8F` |
| Dorado (boya/medalla) | `#E8B04B` |

## QR

Es el QR verificado del proyecto (`assets/qr/qr.svg`), negro sobre blanco, ~17 cm de lado dentro de la tarjeta.
Apunta a `https://enriquepiedfort.waterpoloargentina.com` (no va escrita en el banner: se llega por el QR).
No lo recortes, estires ni le saques el margen blanco.
Va como SVG anidado; si alguna versión vieja de Illustrator no lo importa bien, borralo y colocá
`assets/qr/qr.svg` en el mismo recuadro blanco.
Antes de tirar la impresión final, escanealo desde el PDF/prueba con dos o tres teléfonos.

## Foto

Embebida a partir de `img/gato_profile.png` (864 × 1152 px), reescalada ×2 con enfoque.
Va a sangre completa (85 cm de ancho) en la franja de arriba, alineada por el borde superior y con
la base fundida hacia el azul del fondo. A ese tamaño queda cerca de **50 ppp** — alcanza para un
banner que se mira de lejos, pero si aparece un original de más resolución conviene reemplazarla en
Illustrator (entra en el mismo marco).

## Regenerar

`build_banner.py` arma el SVG y la vista previa. Para reconstruir:
desde la raíz del repo: `python3 banner/build_banner.py` (necesita solo Pillow).
