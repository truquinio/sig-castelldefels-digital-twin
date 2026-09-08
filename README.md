# SIG Castelldefels · Digital Twin

Aplicación web estática orientada a demo municipal y evolución hacia un gemelo digital urbano.

## Qué funciona

- GitHub Pages: `index.html`, `app.js`, `styles.css` en raíz.
- Mapa Leaflet + teselas OpenStreetMap, con límite municipal cargado desde el repositorio original.
- Inventario OSM normalizado con categorías y nombres funcionales cuando el nombre real no está disponible.
- Parkings separados de Bicicleta. Servicios separados de Oficinas. Cine/centros culturales separados de deporte.
- Clustering/agrupación visual de puntos para reducir ruido en zooms bajos.
- Ortofoto ICGC por WMS.
- Parcelario Catastro INSPIRE por WMS.
- Capa de planeamiento MUC preparada por WMS.
- Consulta Catastro mediante `server.py` en local; GitHub Pages mantiene fallback al visor oficial por posibles restricciones CORS.
- Simulador existente vs. máximo teórico.
- Escenario 3D conceptual con Three.js.
- Agente determinista y conexión opcional a Ollama local.
- Exportación JSON del análisis.

## Arranque local

```bash
python server.py
# http://localhost:8000
```

## Catastro

```bash
python scripts/catastro_fetch.py 4304126DF1740C
python scripts/catastro_wfs_fetch.py 4304126DF1740C
```

## Overture

```bash
pip install overturemaps
python scripts/fetch_overture.py --bbox '1.94,41.24,2.03,41.31' --type building --out data/overture_buildings.geojson
```

## Datos y trazabilidad

- Catastro / INSPIRE: fuente oficial.
- Generalitat / MUC: fuente oficial.
- ICGC: fuente oficial.
- OpenStreetMap: dato abierto.
- Overture: dato abierto.
- Cálculos de viabilidad: inferencia/escenario.
- Parámetros normativos no verificados no se presentan como oficiales.

## Próximas evoluciones

1. Parcelario vectorial clicable y cruce automático parcela → zona MUC.
2. Registro normativo completo de Castelldefels con fuente/artículo/página.
3. Censo municipal geocodificado.
4. Overture/ICGC/LiDAR procesados localmente.
5. Cesium + 3D Tiles para gemelo 3D de mayor escala.
6. Agente con herramientas reales y backend seguro.
