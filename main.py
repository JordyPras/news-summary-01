# news-summary-01 entry: writes the summary beside this file to /output/entry.txt.
# Python 3.13, standard library only; no network; deterministic (same bytes every run).
# Normalises line endings so the output is identical however summary.txt was saved,
# and fails loudly instead of writing an empty entry (the gate needs >=1 non-space char).
import os
from pathlib import Path

src = Path(__file__).resolve().parent / "summary.txt"
text = src.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
if not text.strip():
    raise SystemExit("summary.txt is empty")
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(text, encoding="utf-8", newline="\n")
