# Scripts de datos

`catastro_fetch.py` — consulta datos catastrales no protegidos por referencia y genera `data/parcelas.json`.

`catastro_wfs_fetch.py` — descarga geometría de parcela mediante INSPIRE WFS.

`muc_fetch.py` — descarga GetCapabilities del servicio oficial de Planejament de la Generalitat.

`fetch_overture.py` — descarga edificios/lugares Overture por bbox.

`enrich_pois_overture.py` — intenta asignar a puntos OSM sin nombre un nombre de Overture cercano; no sobrescribe nombres existentes y deja la distancia de coincidencia para revisión.

`enrich_pois.py` — crea nombres funcionales seguros para POI sin nombre.
