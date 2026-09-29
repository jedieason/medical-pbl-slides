#!/usr/bin/env python3
"""Narrow PBL deck content audit; not medical/visual validation. Requires lxml."""
import argparse,json,re
from zipfile import ZipFile
from lxml import etree as E
from deck_notes import records,NS

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('pptx');a=p.parse_args();issues=[]
 with ZipFile(a.pptx) as z:
  rec=records(z)
  for x in rec:
   n=x['slide'];root=E.fromstring(z.read(x['slide_part']));refs=x['title'].lower().startswith('references')
   if not x['notes'].strip():issues.append([n,'missing_notes'])
   elif not refs and len(x['notes'])<250:issues.append([n,'review_note_depth',len(x['notes'])])
   foot=[]
   for sh in root.findall('.//p:sp',NS):
    text=' '.join(sh.xpath('.//a:t/text()',namespaces=NS));off=sh.find('p:spPr/a:xfrm/a:off',NS)
    if off is None:continue
    y=int(off.get('y'))/9525;fill=sh.find('p:spPr/a:solidFill/a:srgbClr',NS)
    if text.startswith('Next:') or re.match(r'^\d+\s*·',text):issues.append([n,'old_navigation',text])
    if text.isdigit() and y>600:issues.append([n,'page_number'])
    if fill is not None and fill.get('val','').upper() in ('CAD5C4','C9D4C4','F6AE2D') and y>500:issues.append([n,'old_bottom_bar'])
    if y>650 and text:
     foot.append(text)
     if len(sh.findall('.//a:p',NS))>1 or sh.findall('.//a:br',NS):issues.append([n,'footer_has_explicit_break'])
     if 'Modified from' in text or 'Reproduced from' in text:issues.append([n,'review_attribution_for_direct_screenshot'])
     if 'doi.org' in text:issues.append([n,'long_bibliography_in_footer'])
   if not refs and not foot:issues.append([n,'missing_visible_short_citation'])
 print(json.dumps({'slide_count':len(rec),'notes_characters':sum(len(x['notes']) for x in rec),'findings':issues,'boundary':'Human/model review required: source accuracy, note quality, wrapping and cropping not proven'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
