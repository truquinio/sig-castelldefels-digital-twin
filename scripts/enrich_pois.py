#!/usr/bin/env python3
"""Safe OSM POI naming: replaces 'Sin nombre' only with functional labels, never invented brands."""
import json,sys
from pathlib import Path
TAGS={'amenity=parking':'Parking','amenity=bicycle_parking':'Aparcamiento de bicicletas','amenity=bicycle_rental':'Punto de alquiler de bicicletas','leisure=park':'Parque','leisure=playground':'Área de juegos','leisure=pitch':'Pista deportiva','office=estate_agent':'Agencia inmobiliaria','shop=seafood':'Pescadería','shop=convenience':'Tienda de conveniencia','shop=kiosk':'Kiosco','shop=beauty':'Centro de estética','tourism=information':'Punto de información turística','amenity=cinema':'Cine'}
def main(src,dst):
 d=json.loads(Path(src).read_text(encoding='utf-8'))
 for f in d.get('features',[]):
  p=f.setdefault('properties',{}); n=str(p.get('name') or '').strip(); tag=str(p.get('primary_tag') or '').lower()
  if not n or n.lower() in {'sin nombre','unnamed'}: p['display_name']=TAGS.get(tag,'Punto cartográfico');p['name_quality']='functional'
  else:p['display_name']=n;p['name_quality']='source'
 Path(dst).write_text(json.dumps(d,ensure_ascii=False),encoding='utf-8')
if __name__=='__main__':main(sys.argv[1],sys.argv[2])
