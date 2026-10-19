"""Add /TrimBox (= MediaBox) to every page of a PDF with qpdf's JSON update (no other change).
PDF/X requires a TrimBox on each page object; Ghostscript writes it only on the page tree.
Usage: python3 tools/pdfx/add_trimbox.py in.pdf out.pdf
"""
import json, subprocess, sys, tempfile

src, dst = sys.argv[1], sys.argv[2]
j = json.loads(subprocess.run(["qpdf", "--json-output=2", "--json-stream-data=none", src, "-"],
                              capture_output=True, text=True, check=True).stdout)
objs = j["qpdf"][1]
update = {}
for key, val in objs.items():
    v = val.get("value")
    if isinstance(v, dict) and v.get("/Type") == "/Page":
        box = v.get("/MediaBox", [0, 0, 612, 792])
        v = dict(v)
        v["/TrimBox"] = box
        update[key] = {"value": v}
doc = {"qpdf": [{"jsonversion": 2, "pushedinheritedpageresources": False, "calledgetallpages": False,
                 "maxobjectid": j["qpdf"][0]["maxobjectid"]}, update]}
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
    json.dump(doc, fh)
subprocess.run(["qpdf", src, "--update-from-json=" + fh.name, dst], check=True)
print(f"TrimBox added to {len(update)} pages -> {dst}")
