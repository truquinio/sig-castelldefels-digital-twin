#!/usr/bin/env python3
"""Save current Generalitat PLANEJAMENT WMS capabilities for layer discovery."""
from pathlib import Path
from urllib.request import Request,urlopen
URL='https://sig.gencat.cat/ows/PLANEJAMENT/wms?service=WMS&request=GetCapabilities'
out=Path(__file__).resolve().parents[1]/'data/muc_capabilities.xml'
req=Request(URL,headers={'User-Agent':'SIG-Castelldefels-Digital-Twin/1.0'})
out.write_bytes(urlopen(req,timeout=30).read());print(out)
