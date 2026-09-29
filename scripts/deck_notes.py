#!/usr/bin/env python3
"""Extract/replace existing notes by actual slide order and relationships. Requires lxml."""
import argparse,json,posixpath,copy
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
A='{'+NS['a']+'}';R='{'+NS['r']+'}'
def rels(z,part):
 path=posixpath.join(posixpath.dirname(part),'_rels',posixpath.basename(part)+'.rels')
 if path not in z.namelist():return {}
 root=E.fromstring(z.read(path));out={}
 for x in root:
  if x.get('TargetMode')=='External':continue
  target=x.get('Target');dest=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(part),target))
  out[x.get('Id')]=(dest,x.get('Type'))
 return out

def records(z):
 pres='ppt/presentation.xml';rs=rels(z,pres);out=[]
 for i,s in enumerate(E.fromstring(z.read(pres)).findall('p:sldIdLst/p:sldId',NS),1):
  sp=rs[s.get(R+'id')][0];root=E.fromstring(z.read(sp));title=''
  for shape in root.findall('.//p:sp',NS):
   ph=shape.find('p:nvSpPr/p:nvPr/p:ph',NS)
   if ph is not None and ph.get('type') in ('title','ctrTitle'):
    title=' '.join(shape.xpath('.//a:t/text()',namespaces=NS));break
  if not title:
   # Explicit title boxes in the approved template have no placeholder; choose large text near the top.
   candidates=[]
   for shape in root.findall('.//p:sp',NS):
    text=' '.join(shape.xpath('.//a:t/text()',namespaces=NS));off=shape.find('p:spPr/a:xfrm/a:off',NS)
    if text and off is not None:candidates.append((int(off.get('y')),text))
   if candidates:title=min(candidates)[1]
  np=next((v[0] for v in rels(z,sp).values() if v[1].endswith('/notesSlide')),None)
  body=None
  if np:
   nr=E.fromstring(z.read(np))
   for sh in nr.findall('.//p:sp',NS):
    ph=sh.find('p:nvSpPr/p:nvPr/p:ph',NS)
    if ph is not None and ph.get('type')=='body':body=sh.find('p:txBody',NS);break
  text='\n'.join(''.join(p.xpath('.//a:t/text()',namespaces=NS)) for p in body.findall('a:p',NS)) if body is not None else ''
  out.append({'slide':i,'title':title,'slide_part':sp,'notes_part':np,'notes':text})
 return out

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('mode',choices=['extract','apply']);p.add_argument('pptx',type=Path);p.add_argument('json',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
 with ZipFile(a.pptx) as z:
  rec=records(z)
  if a.mode=='extract':
   with a.json.open('x') as f:json.dump(rec,f,ensure_ascii=False,indent=2)
   return
  if not a.output or a.output.exists():p.error('Specify a new --output PPTX')
  incoming=json.loads(a.json.read_text());assert len(incoming)==len(rec),'Must supply notes for every slide'
  patches={}
  for old,new in zip(rec,incoming):
   assert old['slide']==new['slide'] and old['title']==new['title'],'Slide/title mismatch; re-extract latest deck'
   assert new['notes'].strip(),'Empty notes';assert old['notes_part'],'No existing notes part; create with presentation runtime first'
   root=E.fromstring(z.read(old['notes_part']));body=None
   for sh in root.findall('.//p:sp',NS):
    ph=sh.find('p:nvSpPr/p:nvPr/p:ph',NS)
    if ph is not None and ph.get('type')=='body':body=sh.find('p:txBody',NS);break
   assert body is not None,'No notes body placeholder'
   sample=body.find('.//a:rPr',NS)
   for paragraph in list(body.findall('a:p',NS)):body.remove(paragraph)
   for line in new['notes'].split('\n'):
    paragraph=E.SubElement(body,A+'p');run=E.SubElement(paragraph,A+'r')
    if sample is not None:run.append(copy.deepcopy(sample))
    E.SubElement(run,A+'t').text=line
   patches[old['notes_part']]=E.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
  with ZipFile(a.output,'x',ZIP_DEFLATED) as out:
   for f in z.infolist():out.writestr(f,patches.get(f.filename,z.read(f.filename)))
 with ZipFile(a.output) as result:
  saved=records(result)
  assert [x['notes'] for x in saved]==[x['notes'] for x in incoming],'Saved notes differ'
 print(f'Updated and verified {len(rec)} notes; other ZIP members preserved.')
if __name__=='__main__':main()
