"""Locate card excerpts in local sentence archives without guessing a paper.

Exact/typography-normalized text and explicit ellipsis segments are supported.
Ambiguous text matches and citation conflicts remain visible, never silently
converted into a unique paper identity. This does not verify the original PDF.
"""
import re
from collections import defaultdict
from pathlib import Path

ARCHIVE_REL = 'story-blueprints/v4/rhetoric-moves/sources'
PARA = re.compile(r'<!--\s*para(?:graph)?\s+(\d+)\s*-->')


def normalized(text):
    text = text.replace('“','"').replace('”','"').replace('’',"'").replace('‘',"'")
    text = re.sub(r'\[\^[^]]+\]', '', text)
    text = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', text)
    return ' '.join(text.replace('*','').replace('`','').split()).strip('" ')


def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def excerpt_chunks(text):
    # Remove the card's trailing Chinese annotation, preserving original text
    # separately in the catalog. Explicit ellipses mean non-contiguous parts.
    match = re.search(r'[\u4e00-\u9fff]', text)
    if match:
        text = text[:match.start()].rstrip('（(')
    chunks = [normalized(c) for c in re.split(r'\.{3,}|…+',text)]
    return [c for c in chunks if len(c)>=24 and len(words(c))>=4]


def parse_archive(path, root):
    raw = path.read_text(encoding='utf-8')
    lines = raw.splitlines()
    ck = re.search(r'^citekey:\s*["\']?([^"\'\n]+)',raw,re.M)
    citekey = ck.group(1).strip() if ck else path.name.removesuffix('.sentences.md')
    records, section, para, start, body = [], '', None, 0, []
    def flush(end):
        if body and section:
            text = '\n'.join(body).strip()
            if text:
                records.append({'source_file':path.relative_to(root).as_posix(),
                                'citekey':citekey,'source_section':section,'paragraph_number':para,
                                'source_line':start+1,'source_end_line':end,'text':text})
    for i,line in enumerate(lines):
        marker=PARA.search(line)
        if line.startswith('## ') or marker:
            flush(i)
            body=[]; start=i+1
            if marker:
                para=int(marker.group(1))
            else:
                section=line.lstrip('#').strip(); para=None
        elif section and line.strip() and not line.strip().startswith('<!--'):
            body.append(line)
    flush(len(lines))
    for i,record in enumerate(records):
        record['_normalized']=normalized(record['text'])
        record['_before']=records[i-1] if i and records[i-1]['source_section']==record['source_section'] else None
        record['_after']=records[i+1] if i+1<len(records) and records[i+1]['source_section']==record['source_section'] else None
    return raw,records


def paper_identity(key):
    year=set(re.findall(r'(?:19|20)\d{2}',key))
    lead=re.split(r'[^a-z0-9]+',key.lower())[0]
    lead=re.sub(r'(?:19|20)\d{2}.*','',lead)
    return lead,year


def compatible(record_key, archive_key):
    """Compare key strings; discrepancies are not bibliographic adjudications.

    Archives sometimes use a title as the key, or concatenate author names.
    Accept an author token anywhere in such a key, retaining year checks.
    """
    identities=[paper_identity(k) for k in record_key.split('/')]
    al,ay=paper_identity(archive_key)
    informative=[(lead,years) for lead,years in identities if lead and years]
    if not informative or not al or not ay:
        return None
    tokens=re.findall(r'[a-z]+',archive_key.lower())
    return any(years==ay and (lead in tokens or
               (min(len(lead),len(al))>=3 and (lead.startswith(al) or al.startswith(lead))))
               for lead,years in informative)


def public(record):
    return {k:v for k,v in record.items() if not k.startswith('_')}


def attach_contexts(entries,root,digest):
    chunks_by_uid={r['uid']:excerpt_chunks(r['text']) for r in entries if r['kind']=='verbatim'}
    wanted={tuple(words(c)[:4]) for cs in chunks_by_uid.values() for c in cs}
    prefix_index=defaultdict(list)
    dependencies={}
    for path in sorted((root/ARCHIVE_REL).glob('*.sentences.md')):
        raw,paragraphs=parse_archive(path,root)
        dependencies[path.relative_to(root).as_posix()]=digest(raw)
        for p in paragraphs:
            tokens=words(p['_normalized'])
            hits={tuple(tokens[i:i+4]) for i in range(max(0,len(tokens)-3))} & wanted
            for key in hits:
                prefix_index[key].append(p)
    for row in entries:
        if row['kind']!='verbatim':
            continue
        chunks=chunks_by_uid[row['uid']]
        matches=[]
        if chunks:
            by_file=[]
            for chunk in chunks:
                candidates=prefix_index.get(tuple(words(chunk)[:4]),[])
                found=[p for p in candidates if chunk in p['_normalized']]
                by_file.append({p['source_file'] for p in found})
                matches.append(found)
            common=set.intersection(*by_file) if by_file else set()
        else:
            common=set()
        # Prefer an explicitly compatible paper only among real text matches.
        eligible=[f for f in sorted(common) if compatible(row['citekey'],
            next(p['citekey'] for found in matches for p in found if p['source_file']==f)) is True]
        chosen=eligible if eligible else sorted(common)
        if len(chosen)==1:
            path=chosen[0]
            paragraphs={p['source_line']:p for found in matches for p in found if p['source_file']==path}
            ps=[paragraphs[k] for k in sorted(paragraphs)]
            agreement=compatible(row['citekey'],ps[0]['citekey'])
            ambiguous_location=any(sum(p['source_file']==path for p in found)>1 for found in matches)
            row['source_context']={'state':'citation_discrepancy' if agreement is False else ('ambiguous_paragraph' if ambiguous_location else 'matched'),
                 'verification_level':'local_archive_text_match',
                 'match_method':'segmented_or_typography_normalized' if len(chunks)>1 else 'typography_normalized',
                 'archive_citekey':ps[0]['citekey'],'citation_agreement':agreement,
                 'location_ambiguous':ambiguous_location,
                 'identity_note':'仅比较来源键的作者/年份字符串；差异可能来自别名、发表年份或误归源，须核对书目',
                 'paragraphs':[public(p) for p in ps],
                 'preceding_paragraph':public(ps[0]['_before']) if ps[0]['_before'] else None,
                 'following_paragraph':public(ps[-1]['_after']) if ps[-1]['_after'] else None}
        elif chosen:
            row['source_context']={'state':'ambiguous','candidate_archives':chosen,
                                   'verification_level':'unresolved'}
        else:
            row['source_context']={'state':'not_found','verification_level':'card_only',
                                   'reason':'本地句子档案未逐字定位；不猜来源或原文段落'}
    return dependencies
