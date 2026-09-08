#!/usr/bin/env python3
"""Tiny local server/proxy for public geospatial services.
No keys. Intended for local demo/development. It also serves the static web folder.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import Request, urlopen
from pathlib import Path
import os
ROOT=Path(__file__).resolve().parent
WEB=ROOT/'web'
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw): super().__init__(*a,directory=str(WEB),**kw)
    def do_GET(self):
        u=urlparse(self.path)
        if u.path=='/api/catastro':
            q=parse_qs(u.query); rc=q.get('rc',[''])[0]
            target='https://ovc.catastro.meh.es/ovcservweb/ovcswlocalizacionrc/ovccallejero.asmx/Consulta_DNPRC?'+urlencode({'Provincia':'Barcelona','Municipio':'Castelldefels','RC':rc})
            return self.proxy(target,'text/xml; charset=utf-8')
        if u.path=='/api/muc/capabilities':
            target='https://sig.gencat.cat/ows/PLANEJAMENT/wms?service=WMS&request=GetCapabilities'
            return self.proxy(target,'text/xml; charset=utf-8')
        return super().do_GET()
    def proxy(self,url,ctype):
        try:
            req=Request(url,headers={'User-Agent':'SIG-Castelldefels-Digital-Twin/1.0'})
            data=urlopen(req,timeout=25).read()
            self.send_response(200);self.send_header('Content-Type',ctype);self.send_header('Access-Control-Allow-Origin','*');self.end_headers();self.wfile.write(data)
        except Exception as e:
            self.send_error(502,f'Proxy error: {e}')
if __name__=='__main__':
    os.chdir(WEB);print('SIG Castelldefels Digital Twin: http://localhost:8000');ThreadingHTTPServer(('127.0.0.1',8000),Handler).serve_forever()
