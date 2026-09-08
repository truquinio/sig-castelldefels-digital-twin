#!/usr/bin/env python3
"""Fetch official Catastro INSPIRE cadastral parcel geometry by reference.
Output is raw GML so the project does not require geopandas/shapely to run the fetch step.
"""
import argparse, pathlib, urllib.parse, urllib.request
URL='https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx'
def main():
 p=argparse.ArgumentParser();p.add_argument('refcat');p.add_argument('-o','--out',default='data/catastro_parcela.gml');a=p.parse_args()
 q=urllib.parse.urlencode({'service':'wfs','version':'2','request':'getfeature','STOREDQUERIE_ID':'GetParcel','refcat':a.refcat,'srsname':'EPSG:25830'})
 req=urllib.request.Request(URL+'?'+q,headers={'User-Agent':'SIG-Castelldefels-Digital-Twin/1.0'})
 data=urllib.request.urlopen(req,timeout=30).read();out=pathlib.Path(a.out);out.parent.mkdir(exist_ok=True);out.write_bytes(data);print(out)
if __name__=='__main__':main()
