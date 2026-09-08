# SIG Castelldefels · Digital Twin

Copia independiente orientada a demostración municipal y evolución hacia un gemelo digital urbano.

## Núcleo
- 2D/3D web con MapLibre + OpenFreeMap.
- Fallback raster OSM para evitar mapas vacíos si falla el estilo vectorial.
- Actividades OSM normalizadas, clustering y categorías separadas.
- Ortofoto ICGC.
- Parcelario Catastro INSPIRE como capa WMS y scripts WFS.
- Planeamiento MUC de la Generalitat como capa WMS y descubrimiento de capas vía GetCapabilities.
- Catastro OVC por referencia catastral (datos no protegidos), con proxy local opcional.
- Motor existente vs. máximo teórico y generación de volumen 3D conceptual.
- Agente geoespacial determinista + conexión opcional a Ollama local.
- Descarga de análisis JSON.
- Overture: scripts preparados para descargar edificios/lugares por bbox.

## Arranque local
```bash
python server.py
# abrir http://localhost:8000
```

## Catastro por RC
```bash
python scripts/catastro_fetch.py 4304126DF1740C
```

## Parcela INSPIRE WFS
```bash
python scripts/catastro_wfs_fetch.py 4304126DF1740C
```

## Overture
Instalar `overturemaps` y usar, por ejemplo:
```bash
python scripts/fetch_overture.py --bbox '1.94,41.24,2.03,41.31' --type building --out data/overture_buildings.geojson
```

## Planeamiento
La Generalitat publica servicios WMS/WFS del ámbito de planeamiento y descargas estructuradas del MUC. Antes de fijar automáticamente reglas normativas por parcela, descargar y validar el instrumento vigente y sus modificaciones.

## IA
No se publica ninguna API key. El agente funciona de forma determinista sobre el contexto disponible. Si se desea LLM local, instalar Ollama y un modelo local; la interfaz llama a `http://localhost:11434`.

## Estado normativo
No se presentan parámetros no verificados como oficiales. `data/normative_registry.example.json` es solamente una plantilla.
