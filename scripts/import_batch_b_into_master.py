#!/usr/bin/env python3
"""Insert P-10..P-19 source-ledger dossiers into the 41-opportunity master Word.

Only Markdown in research/dossiers/P-10..P-19 is imported. This gives the master document
self-contained, product-specific source ledgers and preserves the earlier generic spine as a
transparent scaffold. Re-running without restoring a pre-import document would duplicate
content; this is deliberately a one-time Batch B import script.
"""
from pathlib import Path
import re
from copy import deepcopy
from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.shared import Pt

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "reports" / "گزارش_جامع_۴۱_فرصت_پلتفرمی_مد_و_پوشاک_ایران.docx"
DOSSIERS = ROOT / "research" / "dossiers"


def set_rtl(paragraph):
    """Set paragraph bidi/XML language conservatively without relying on Word UI."""
    ppr = paragraph._p.get_or_add_pPr()
    bidi = OxmlElement("w:bidi")
    ppr.append(bidi)
    for run in paragraph.runs:
        rpr = run._r.get_or_add_rPr()
        rtl = OxmlElement("w:rtl")
        rtl.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val", "1")
        rpr.append(rtl)


def clean_markup(text):
    """Remove the controlled Markdown emphasis markers from prose."""
    return text.replace("**", "")


def paragraph(fragment, text="", style=None, bold_prefix=None):
    p = fragment.add_paragraph(style=style)
    text = clean_markup(text)
    if bold_prefix and text.startswith(bold_prefix):
        p.add_run(bold_prefix).bold = True
        p.add_run(text[len(bold_prefix):])
    else:
        p.add_run(text)
    set_rtl(p)
    return p


def parse_table(lines, i, fragment):
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        # Markdown alignment separator
        if not all(re.match(r"^:?-{3,}:?$", c.replace(" ", "")) for c in cells):
            rows.append(cells)
        i += 1
    if rows:
        width = max(len(r) for r in rows)
        tbl = fragment.add_table(rows=0, cols=width)
        tbl.style = "Table Grid"
        for row_no, cells in enumerate(rows):
            cells = cells + [""] * (width - len(cells))
            row = tbl.add_row().cells
            for idx, val in enumerate(cells):
                row[idx].text = val
                for p in row[idx].paragraphs:
                    set_rtl(p)
                    for run in p.runs:
                        run.font.size = Pt(8)
                        if row_no == 0:
                            run.bold = True
    return i


def markdown_to_fragment(md_path):
    """Minimal deterministic Markdown-to-Word converter for these controlled dossiers."""
    lines = md_path.read_text(encoding="utf-8").splitlines()
    fragment = Document()
    paragraph(fragment, "پروندهٔ مستقل پژوهش اسنادی پایه", style="Heading 1")
    # Do not re-import top-level title: master has P-xx heading/title already.
    skip_title = True
    i = 0
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if not s or s == "---":
            i += 1
            continue
        if s.startswith("|"):
            i = parse_table(lines, i, fragment)
            continue
        if s.startswith("# ") and skip_title:
            skip_title = False
            i += 1
            continue
        if s.startswith("### "):
            paragraph(fragment, s[4:], style="Heading 3")
        elif s.startswith("## "):
            paragraph(fragment, s[3:], style="Heading 2")
        elif s.startswith("# "):
            paragraph(fragment, s[2:], style="Heading 1")
        elif s.startswith("> "):
            p = paragraph(fragment, s[2:])
            p.style = "Quote" if "Quote" in [st.name for st in fragment.styles] else p.style
        elif re.match(r"^[-*] ", s):
            # Keep visible bullets even if the document style lacks a Persian list definition.
            paragraph(fragment, "• " + s[2:])
        elif re.match(r"^\d+\. ", s):
            paragraph(fragment, s)
        else:
            paragraph(fragment, s)
        i += 1
    return fragment


def insert_before(master_doc, before_p, fragment):
    body = master_doc._element.body
    index = list(body).index(before_p._p)
    for child in list(fragment._element.body):
        if child.tag.endswith("}sectPr"):
            continue
        body.insert(index, deepcopy(child))
        index += 1


def clear_between(master_doc, first_p, before_p):
    """Delete the generic scaffold after a P heading but preserve both dossier headings."""
    body = master_doc._element.body
    children = list(body)
    start = children.index(first_p._p)
    end = children.index(before_p._p)
    for child in children[start + 1:end]:
        body.remove(child)


def heading(doc, prefix):
    for p in doc.paragraphs:
        if p.text.strip().startswith(prefix + " —"):
            return p
    raise ValueError(f"Could not find dossier heading {prefix}")


def next_heading(doc, pid):
    n = int(pid.split("-")[1]) + 1
    prefix = f"پ-{n:02d}".replace("0", "۰").replace("1", "۱").replace("2", "۲").replace("3", "۳").replace("4", "۴").replace("5", "۵").replace("6", "۶").replace("7", "۷").replace("8", "۸").replace("9", "۹")
    # Existing report uses Persian zero and Persian digits exactly.
    for p in doc.paragraphs:
        if p.text.strip().startswith(prefix + " —"):
            return p
    raise ValueError(f"Could not find next dossier heading after {pid}: expected {prefix}")


def main():
    doc = Document(MASTER)
    # Work from high to low to avoid any human/paragraph lookup ambiguity after insertion.
    for n in range(19, 9, -1):
        pid = f"P-{n:02d}"
        matches = sorted(DOSSIERS.glob(pid + "_*.md"))
        if len(matches) != 1:
            raise ValueError(f"Expected exactly one dossier for {pid}, got {matches}")
        boundary = next_heading(doc, pid)
        current = heading(doc, pid.replace("P-", "پ-").translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")))
        clear_between(doc, current, boundary)
        fragment = markdown_to_fragment(matches[0])
        insert_before(doc, boundary, fragment)
        print("replaced scaffold for", pid, matches[0].name)
    doc.save(MASTER)
    print("saved", MASTER)

if __name__ == "__main__":
    main()
