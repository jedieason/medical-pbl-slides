#!/usr/bin/env python3
"""Render a PDF page region and save provenance. Requires pypdfium2 and Pillow."""
import argparse,json,hashlib
from pathlib import Path
import pypdfium2 as pdfium

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf',type=Path);p.add_argument('output',type=Path);p.add_argument('--page',required=True,type=int,help='Zero-based PDF page index');p.add_argument('--box',nargs=4,type=float,default=[0,0,1,1],metavar=('LEFT','TOP','RIGHT','BOTTOM'),help='Normalized top-left-origin bounds');p.add_argument('--scale',type=float,default=3);p.add_argument('--source-id',required=True);p.add_argument('--figure',required=True);a=p.parse_args()
 l,t,r,b=a.box
 if not(0<=l<r<=1 and 0<=t<b<=1 and 0<a.scale<=8):p.error('Invalid crop or scale')
 meta=Path(str(a.output)+'.source.json')
 if a.output.exists() or meta.exists():p.error('Output exists')
 doc=pdfium.PdfDocument(a.pdf)
 if not 0<=a.page<len(doc):p.error('Page out of range')
 page=doc[a.page];bitmap=page.render(scale=a.scale);im=bitmap.to_pil();w,h=im.size
 crop=im.crop((round(l*w),round(t*h),round(r*w),round(b*h)))
 a.output.parent.mkdir(parents=True,exist_ok=True);crop.save(a.output,format='PNG')
 meta.write_text(json.dumps({'source_id':a.source_id,'figure':a.figure,'pdf':str(a.pdf.resolve()),'sha256':hashlib.sha256(a.pdf.read_bytes()).hexdigest(),'page_index':a.page,'box_normalized_top_left':a.box,'scale':a.scale,'pixels':crop.size,'inspection_required':'Verify caption, labels and retained scientific meaning'},ensure_ascii=False,indent=2))
 bitmap.close();page.close();doc.close();print(str(a.output))
if __name__=='__main__':main()
