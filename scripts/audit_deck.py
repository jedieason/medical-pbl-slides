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
   relpart=x['slide_part'].replace('ppt/slides/','ppt/slides/_rels/')+'.rels'
   targets={e.get('Id'):e.get('Target') for e in E.fromstring(z.read(relpart))} if relpart in z.namelist() else {}
   foot=[]
   for sh in root.findall('.//p:sp',NS):
    for run in sh.findall('.//a:r',NS):
     rt=''.join(run.xpath('./a:t/text()',namespaces=NS));rp=run.find('a:rPr',NS)
     if rp is None:continue
     linked=rp.find('a:hlinkClick',NS) is not None
     is_anchor=bool(re.fullmatch(r'https?://\S+|(?:\[)?Link(?:\])?',rt.strip()))
     xy=sh.find('p:spPr/a:xfrm/a:off',NS)
     is_citation=refs or sh.find('p:nvSpPr/p:cNvPr',NS).get('name','')=='citation' or (xy is not None and int(xy.get('y'))/9525>=650)
     if is_citation and linked and not is_anchor:issues.append([n,'citation_prose_hyperlinked',rt])
     if is_citation and linked and rt.strip().startswith(('http://','https://')) and targets.get(rp.find('a:hlinkClick',NS).get('{'+NS['r']+'}id'))!=rt.strip():issues.append([n,'url_hyperlink_target_mismatch',rt])
     if is_citation and rp.get('u','none') not in ('none','') and not is_anchor:issues.append([n,'citation_prose_underlined',rt])
    text=' '.join(sh.xpath('.//a:t/text()',namespaces=NS));off=sh.find('p:spPr/a:xfrm/a:off',NS)
    if off is None:continue
    y=int(off.get('y'))/9525
    if y>600 and re.search(r'\d{2,3}-[12]-醫學',text) and not re.fullmatch(r'\d{2,3}-[12]-醫學[（(][一二][）)]',re.sub(r'\s','',text)):issues.append([n,'exam_source_label_extra_metadata',text])
    fill=sh.find('p:spPr/a:solidFill/a:srgbClr',NS)
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
