from pathlib import Path
import re,json

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'original/prime_average_lecture'
types='theorem|lemma|proposition|corollary|definition|example|remark'
blocks={}; index={}
for file in sorted((SOURCE/'chapters').glob('*.tex')):
    text=file.read_text(encoding='utf-8-sig')
    items=[]
    pattern=re.compile(r'\\begin\{('+types+r')\}(?:\[[^\]]*\])?')
    for num,m in enumerate(pattern.finditer(text),1):
        end=text.index('\\end{'+m[1]+'}',m.end())+len('\\end{'+m[1]+'}')
        body=text[m.start():end]
        label=re.search(r'\\label\{([^}]+)\}',body)
        key=label[1] if label else file.stem+'-unit'+str(num)
        match=re.match(r'\s*\\begin\{proof\}(?:\[[^\]]*\])?',text[end:])
        if match:
            proofend=text.index(r'\end{proof}',end+match.end())+len(r'\end{proof}')
            body=text[m.start():proofend]
            end=proofend
        blocks[key]={'file':file.name,'kind':m[1],'text':body}
        items.append(key)
    index[file.name]=items
    if file.stem.startswith('18_'):
        start=text.index(r'\begin{proof}')
        end=text.index(r'\end{proof}',start)+len(r'\end{proof}')
        blocks['main-proof']={'file':file.name,'kind':'proof','text':text[start:end]}
        index[file.name].append('main-proof')
(HERE/'proof_blocks.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(HERE/'proof_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(index,ensure_ascii=False,indent=2))
