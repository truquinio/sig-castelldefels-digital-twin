#!/usr/bin/env python3
"""Download Overture buildings/places for an AOI using the free overturemaps client."""
import argparse, subprocess, sys

def main():
    p=argparse.ArgumentParser();p.add_argument('--bbox',required=True,help='west,south,east,north');p.add_argument('--type',default='building',choices=['building','place']);p.add_argument('--out',required=True);a=p.parse_args()
    cmd=['overturemaps','download','--bbox',a.bbox,'-f','geojson','--type',a.type,'-o',a.out]
    raise SystemExit(subprocess.call(cmd))
if __name__=='__main__':main()
