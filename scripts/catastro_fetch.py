#!/usr/bin/env python3
"""Fetch public non-protected Catastro data for Castelldefels.
Uses official OVC services documented by the Spanish General Directorate for Cadastre.
Usage: python scripts/catastro_fetch.py 4304126DF1740C [NEXT_RC ...]
"""
import json, re, sys, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path
BASE='https://ovc.catastro.meh.es/ovcservweb/ovcswlocalizacionrc/ovccallejero.asmx/Consulta_DNPRC'
COORD='https://ovc.catastro.meh.es/ovcservweb/OVCWcfCallejero/COVCCoordenadas.svc/rest/Consulta_CPMRC'
OUT=Path(__file__).resolve().parents[1]/'data/parcelas.json'

def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'SIG-Castelldefels-Digital-Twin/1.0'})
    with urllib.request.urlopen(req,timeout=30) as r:return r.read().decode('utf-8','ignore')

def txt(root,*names):
    for e in root.iter():
        tag=e.tag.rsplit('}',1)[-1]
        if tag.lower() in {n.lower() for n in names} and (e.text or '').strip(): return (e.text or '').strip()
    return ''

def parse(rc,xml):
    root=ET.fromstring(xml); uses=[]; built=0; residential=0; commercial=0; parking=0; floors=set()
    for e in root.iter():
        tag=e.tag.rsplit('}',1)[-1].lower()
        if tag not in {'csd','elem','lcsd'}: continue
        use=txt(e,'lcuso','uso'); surf=txt(e,'sconstruida','superficie')
        try:s=float(surf.replace(',','.')) if surf else None
        except:s=None
        if s is None: continue
        uses.append({'use':use,'area_m2':s}); built+=s
        if re.search(r'resid',use,re.I): residential+=s
        if re.search(r'comerc',use,re.I): commercial+=s
        if re.search(r'almac|garaje|aparc',use,re.I): parking+=s
    try: site=float(txt(root,'sfc','supfinca','superficie').replace(',','.'))
    except: site=None
    return {'rc':rc,'site_area_m2':site,'existing_built_m2':built or None,'residential_m2':residential or None,'commercial_m2':commercial or None,'parking_m2':parking or None,'uses':uses,'address':txt(root,'ldt') or None,'year':txt(root,'antiguedad') or None}

def coords(rc):
    q=urllib.parse.urlencode({'Provincia':'Barcelona','Municipio':'Castelldefels','SRS':'EPSG:4326','RefCat':rc[:14]})
    try:
        x=ET.fromstring(get(COORD+'?'+q));
        xc=txt(x,'xcen'); yc=txt(x,'ycen')
        return [float(xc),float(yc)] if xc and yc else None
    except Exception:return None

def main():
    rcs=[re.sub(r'\s+','',x).upper() for x in sys.argv[1:]]
    if not rcs: raise SystemExit('Uso: python scripts/catastro_fetch.py RC [RC2 ...]')
    out=[]
    for rc in rcs:
        q=urllib.parse.urlencode({'Provincia':'Barcelona','Municipio':'Castelldefels','RC':rc})
        d=parse(rc,get(BASE+'?'+q)); d['coords']=coords(rc); out.append(d); print(rc, 'OK')
    OUT.parent.mkdir(exist_ok=True); OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8'); print(f'Escrito {OUT}')
if __name__=='__main__':main()
