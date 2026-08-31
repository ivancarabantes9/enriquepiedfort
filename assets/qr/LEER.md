# Código QR — enriquepiedfort.waterpoloargentina.com

Apunta a: **https://enriquepiedfort.waterpoloargentina.com**
Verificado: decodifica exactamente esa URL (QR versión 4, corrección de errores nivel Q ≈ 25%).

## Qué archivo mandar a la imprenta

| Archivo | Para qué |
|---|---|
| **`qr.svg`** | El que hay que usar en el banner. Vectorial: se agranda a cualquier tamaño sin perder nitidez. Negro sobre blanco. |
| `qr-marca.svg` | Igual pero en azul de marca (`#04263A`) sobre blanco. Escanea bien; usalo solo si el diseño lo pide. |
| `qr-transparente.svg` | Módulos negros sin fondo. Solo si va sobre un color claro y parejo. |
| `qr.eps` / `qr.pdf` | Mismo QR vectorial en los formatos que a veces pide la gráfica. |
| `qr.png` | Respaldo en alta (3690 px). Usar solo si no aceptan vectores. |

## Tamaño en el banner

Al ser vectorial no tiene una medida fija, pero sí un **mínimo** según desde qué distancia se va a escanear:

> lado del QR ≈ distancia de lectura ÷ 10

- Se lee de cerca (~30 cm): mínimo **3 cm**.
- Banner de vereda, se lee a ~1,5 m: mínimo **15 cm**.
- Banner grande, se lee a ~3 m: mínimo **30 cm**.

Recomendado para un banner: **entre 15 y 25 cm de lado**, y cuanto más grande mejor.

## Reglas para que escanee siempre

- **Dejar aire alrededor:** un margen blanco de al menos el 10% del lado del QR (el archivo ya trae ese margen; no lo recortes ni pongas texto encima).
- Buen contraste: QR oscuro sobre fondo claro. No invertir (claro sobre oscuro no lo leen muchos teléfonos).
- No estirar: mantener el cuadrado (proporción 1:1).
- Poner una llamada corta al lado, tipo "Escaneá para conocer su historia".
- Antes de mandar a imprimir 100 banners: pedí una prueba y escaneala con dos o tres teléfonos distintos.

## Regenerar el QR

```
pip install segno
python -c "import segno; segno.make('https://enriquepiedfort.waterpoloargentina.com', error='q').save('qr.svg', scale=10, border=4)"
```
