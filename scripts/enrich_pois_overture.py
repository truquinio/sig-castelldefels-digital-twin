#!/usr/bin/env python3
"""Enrich unlabeled OSM POIs with nearby Overture Places names when available.
Never overwrites an OSM name. Matching is distance-based and can be reviewed afterwards.
"""
import json,math,argparse

def coord(f):
 g=f.get('geometry',{}); c=g.get('coordinates',[]); return (c[0],c[1]) if g.get('type')=='Point' and len(c)>=2 else None

def hav(a,b):
 lon1,lat1=a;lon2,lat2=b; x=math.radians(lon2-lon1)*math.cos(math.radians((lat1+lat2)/2)); y=math.radians(lat2-lat1); return 6371000*math.hypot(x,y)

def main():
 p=argparse.ArgumentParser();p.add_argument('--osm',required=True);p.add_argument('--overture',required=True);p.add_argument('--out',required=True);p.add_argument('--max-m',type=float,default=40);a=p.parse_args()
 osm=json.load(open(a.osm,encoding='utf-8')); ov=json.load(open(a.overture,encoding='utf-8'))
 places=[]
 for f in ov.get('features',[]):
  c=coord(f); props=f.get('properties',{}); name=props.get('name') or props.get('names',{}).get('primary') if isinstance(props.get('names'),dict) else props.get('name')
  if c and name: places.append((c,str(name)))
 matches=0
 for f in osm.get('features',[]):
  p0=f.setdefault('properties',{}); n=str(p0.get('name') or '').strip().lower(); c=coord(f)
  if c and (not n or n in {'sin nombre','unnamed'}):
   best=min(((hav(c,pc),name) for pc,name in places),default=(999999,None))
   if best[1] and best[0]<=a.max_m:p0['enriched_name']=best[1];p0['enrichment_distance_m']=round(best[0],1);matches+=1
 open(a.out,'w',encoding='utf-8').write(json.dumps(osm,ensure_ascii=False,indent=2))
 print(f'Enriquecidos: {matches}')
if __name__=='__main__':main()
