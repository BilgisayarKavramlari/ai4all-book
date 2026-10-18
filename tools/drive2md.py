# usage: drive2md.py <tool-result-json> <out.md> <source-line>
import json, base64, sys, zipfile, io, re, subprocess, tempfile, os
d = json.load(open(sys.argv[1]))
raw = base64.b64decode(d["content"])
mt = d.get("mimeType", "")
if raw[:2] == b"PK":
    z = zipfile.ZipFile(io.BytesIO(raw))
    xml = z.read("word/document.xml").decode("utf8")
    paras = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
        t = (t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
              .replace("&quot;", '"').replace("&apos;", "'"))
        if t.strip():
            paras.append(t.strip())
    text = "\n\n".join(paras)
elif raw[:4] == b"%PDF":
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        f.write(raw); pdf = f.name
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    os.unlink(pdf)
else:
    text = raw.decode("utf8", "replace")
open(sys.argv[2], "w").write(sys.argv[3] + "\n\n" + text + "\n")
print(d.get("title"), mt, "->", sys.argv[2], len(text.split()), "words")
