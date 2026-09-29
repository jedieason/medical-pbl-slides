#!/usr/bin/env python3
"""Download a verified PDF without browser cookies. Requires pypdf."""
import argparse, hashlib, json, tempfile, os
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from datetime import datetime, timezone
from pypdf import PdfReader

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('url');p.add_argument('output',type=Path);p.add_argument('--timeout',type=int,default=30);p.add_argument('--max-mb',type=int,default=100);a=p.parse_args()
 if urlparse(a.url).scheme not in ('http','https'):p.error('HTTP(S) URLs only')
 meta=Path(str(a.output)+'.source.json')
 if a.output.exists() or meta.exists():p.error('Output/provenance exists; reuse or select a new filename')
 a.output.parent.mkdir(parents=True,exist_ok=True);tmp=None
 try:
  with urlopen(Request(a.url,headers={'User-Agent':'MedicalPBLResearch/1.0'}),timeout=a.timeout) as r:
   final_url=r.url;ct=r.headers.get('Content-Type','');size=0
   with tempfile.NamedTemporaryFile(dir=a.output.parent,delete=False) as f:
    tmp=Path(f.name)
    while True:
     b=r.read(1024*1024)
     if not b:break
     size+=len(b)
     if size>a.max_mb*1024*1024:raise ValueError('Size limit exceeded')
     f.write(b)
  with tmp.open('rb') as f:
   if not f.read(1024).lstrip().startswith(b'%PDF-'):raise ValueError('Not a PDF; likely login/HTML response')
  reader=PdfReader(tmp);pages=len(reader.pages)
  if not pages:raise ValueError('No pages')
  sample=(reader.pages[0].extract_text() or '')[:1500]
  record={'requested_url':a.url,'resolved_url':final_url,'content_type':ct,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'bytes':size,'pages':pages,'sha256':hashlib.sha256(tmp.read_bytes()).hexdigest(),'first_page_text_preview':sample,'access_route':'direct HTTP; no browser session','identity_check':'Model must verify title/DOI against expected article'}
  # Exclusive creation prevents accidental overwrite even if another process writes meanwhile.
  with a.output.open('xb') as dst:dst.write(tmp.read_bytes())
  with meta.open('x') as dst:json.dump(record,dst,ensure_ascii=False,indent=2)
  print(json.dumps({'path':str(a.output),'pages':pages,'provenance':str(meta)}))
 finally:
  if tmp is not None:tmp.unlink(missing_ok=True)
if __name__=='__main__':main()
