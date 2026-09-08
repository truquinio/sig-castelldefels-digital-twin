# Arquitectura funcional · SIG Castelldefels PRO

## Módulos

- `web/`: interfaz estática del gemelo digital.
- `data/` (en el repositorio base): GeoJSON de demostración.
- `postgis/`: consultas y análisis espaciales del proyecto base.
- `scripts/`: extracción/preparación de datos del proyecto base.

## Capas de producto

### 1. Cartografía
MapLibre + estilo vectorial público.

### 2. Contexto territorial
ICGC WMS de ortofoto.

### 3. Actividad urbana
POI OSM del dataset de demostración + filtros.

### 4. Analítica
Malla, conteos, categorías y lectura rápida.

### 5. 3D
Extrusión de edificios desde la fuente vectorial de fondo cuando existe geometría/altura utilizable.

### 6. Escenario
Modelo matemático sencillo y explícito:

`ocupación = superficie_suelo × cobertura`

`volumen = ocupación × altura`

No es edificabilidad urbanística ni cálculo normativo.

### 7. 4D
La interfaz incorpora una referencia temporal, pero no simula cambios históricos sin datos históricos reales.

## Próxima integración técnica

```text
QGIS / ETL
   ↓
GeoParquet / PostGIS
   ↓
API/tiles propios
   ↓
MapLibre (2D/2.5D)
   +
CesiumJS (3D/3D Tiles)
   ↓
Agente geoespacial
```

La separación permite que un Ayuntamiento use el mismo frontend con fuentes de datos distintas.
