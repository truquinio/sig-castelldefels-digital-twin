# Handoff para Claude Code

## Regla principal
NO MODIFICAR NUNCA EL REPOSITORIO ORIGINAL `truquinio/sig-castelldefels`.
Trabajar exclusivamente sobre esta copia.

## Objetivo
Convertir el prototipo en `SIG Castelldefels Digital Twin`: Catastro + parcelario + planeamiento + actividades + 3D + escenarios + GeoBI + agente geoespacial.

## Estado actual
- MapLibre/OpenFreeMap + fallback OSM raster.
- Actividades OSM normalizadas y agrupadas.
- Parkings y bicicleta separados.
- Ortofoto ICGC.
- WMS Catastro INSPIRE como capa.
- WMS Planejament Generalitat como capa, con descubrimiento de layer vía GetCapabilities en modo local.
- Consulta Catastro por RC con `/api/catastro` en servidor local y fallback directo.
- Scripts OVC/INSPIRE, MUC y Overture.
- Simulador existente vs. máximo teórico.
- Volumen 3D conceptual.
- Agente determinista + Ollama local opcional.
- Laboratorio CesiumJS sin Ion.

## Próximo orden obligatorio
1. Integrar parcelario INSPIRE WFS de forma robusta y asociar RC al clic de parcela.
2. Descargar/parsear datos MUC del municipio y vincular parcela → clave urbanística; no inventar reglas.
3. Crear registro normativo versionado por zona con fuente, artículo, documento y fecha.
4. Geocodificar el Censo municipal y conservar fuente/confianza.
5. Construir análisis de parcela completo: Catastro + planeamiento + actividades + contexto.
6. Generar envolvente 3D respetando geometría real de parcela, no un rectángulo arbitrario.
7. Añadir Overture como enriquecimiento de edificios/lugares, sin sobreescribir fuentes primarias.
8. Añadir LiDAR/3D Tiles/Cesium solo cuando el pipeline 2D y parcelario esté sólido.
9. Implementar agente con herramientas reales, manteniendo trazabilidad.

## Reglas de datos
- Nunca mezclar `official`, `open`, `inference`, `scenario`.
- Nunca inventar nombres comerciales.
- Nunca presentar una estimación como dato oficial.
- Nunca presentar un volumen conceptual como licencia o informe urbanístico.
- No contar viviendas a partir de superficie residencial agregada si la fuente no individualiza unidades.
