import os, re, sys
root=sys.argv[1]; only=sys.argv[2:] 
ids=sorted(f[:-4] for f in os.listdir(f"{root}/figures/out/color") if f.endswith(".svg"))
if only: ids=[i for i in ids if any(o in i for o in only)]
def inl(p,k,tag):
    s=open(p).read()
    s=re.sub(r'<\?xml[^>]*>','',s); s=re.sub(r'<!DOCTYPE[^>]*>','',s,flags=re.S)
    s=re.sub(r'(<svg[^>]*?)\swidth="[^"]*"',r'\1',s,count=1); s=re.sub(r'(<svg[^>]*?)\sheight="[^"]*"',r'\1',s,count=1)
    for pid in ("hatch","dots","arrow-color","arrow-gray"):
        s=s.replace(f'id="{pid}"',f'id="{pid}{tag}{k}"').replace(f'url(#{pid})',f'url(#{pid}{tag}{k})')
    return s
out=[f'<h3>{i}</h3><div class="r"><div>{inl(f"{root}/figures/out/color/{i}.svg",k,"c")}</div><div>{inl(f"{root}/figures/out/gray/{i}.svg",k,"g")}</div></div>' for k,i in enumerate(ids)]
open(f"{root}/build/preview/figs.html","w").write('<!doctype html><meta charset="utf-8"><title>figures</title><style>body{font:14px system-ui;background:#fff;color:#111;margin:10px}.r{display:flex;gap:10px}.r>div{width:49%;border:1px solid #ccc}.r svg{width:100%;height:auto;display:block}</style>'+"".join(out))
print(len(ids))
