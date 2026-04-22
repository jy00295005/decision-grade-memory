from __future__ import annotations

import html
import re
from pathlib import Path

from PIL import Image as PILImage
from markdown import markdown
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    Image,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path("/Users/chen/Documents/学术/AIResearch/bridging growth-garap based ai for sme")
SOURCE = ROOT / "manuscript/sections/short_paper_conference_export.md"
HTML_OUT = ROOT / "manuscript/sections/short_paper_conference_export.html"
PDF_OUT = ROOT / "output/pdfs/short_paper_conference_formal.pdf"


def clean_inline(text: str) -> str:
    return text.replace("`", "").replace(r"\tau", "τ").replace("->", "→")


def build_html(source_text: str) -> str:
    source_text = clean_inline(source_text)
    source_text = re.sub(
        r"\$\$\s*(.*?)\s*\$\$",
        lambda m: f'\n<div class="equation">{html.escape(m.group(1)).replace("\\tau", "τ").replace("\\\\tau", "τ")}</div>\n',
        source_text,
        flags=re.S,
    )
    body = markdown(
        source_text,
        extensions=["tables", "sane_lists"],
        output_format="html5",
    )
    title = html.escape(source_text.splitlines()[0].lstrip("# ").strip())
    css = """
    @page { size: A4; margin: 2cm 2cm 2.2cm 2cm; }
    body { font-family: Georgia, 'Times New Roman', serif; color: #111; line-height: 1.42; font-size: 11.5pt; }
    h1 { font-size: 20pt; text-align: center; margin: 0 0 18pt 0; }
    h2 { font-size: 15pt; margin: 20pt 0 10pt 0; }
    h3 { font-size: 12.5pt; margin: 14pt 0 8pt 0; }
    p { margin: 0 0 9pt 0; text-align: justify; }
    .equation { text-align: center; font-style: italic; font-size: 12pt; margin: 10pt 0 12pt 0; }
    img { max-width: 100%; display: block; margin: 12pt auto 6pt auto; }
    em { color: #333; }
    table { width: 100%; border-collapse: collapse; margin: 10pt 0 12pt 0; font-size: 10pt; }
    th, td { border: 1px solid #999; padding: 5px 6px; vertical-align: top; }
    th { background: #f2f2f2; }
    ul { margin: 6pt 0 10pt 20pt; }
    """
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>{css}</style>
</head>
<body>
{body}
</body>
</html>
"""


def parse_table(lines: list[str], start: int) -> tuple[Table, int]:
    table_lines = []
    i = start
    while i < len(lines) and lines[i].startswith("|"):
        table_lines.append(lines[i])
        i += 1

    rows = []
    for idx, line in enumerate(table_lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if idx == 1 and all(set(c) <= {"-", ":"} for c in cells):
            continue
        rows.append([clean_inline(c) for c in cells])

    tbl = Table(rows, repeatRows=1)
    tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f0f0")),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
                ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("LEADING", (0, 0), (-1, -1), 11),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return tbl, i


def scale_image(path: Path, max_width: float, max_height: float) -> Image:
    with PILImage.open(path) as img:
        width, height = img.size
    ratio = min(max_width / width, max_height / height)
    return Image(str(path), width=width * ratio, height=height * ratio)


def build_pdf(source_text: str) -> None:
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "PaperTitle",
        parent=styles["Title"],
        fontName="Times-Bold",
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        spaceAfter=14,
    )
    h1_style = ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontName="Times-Bold",
        fontSize=15,
        leading=18,
        spaceBefore=16,
        spaceAfter=8,
    )
    h2_style = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Times-Bold",
        fontSize=12,
        leading=15,
        spaceBefore=12,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Times-Roman",
        fontSize=10.5,
        leading=13.5,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )
    caption_style = ParagraphStyle(
        "Caption",
        parent=body_style,
        fontName="Times-Italic",
        fontSize=9,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#333333"),
        spaceAfter=8,
    )
    equation_style = ParagraphStyle(
        "Equation",
        parent=body_style,
        fontName="Times-Italic",
        fontSize=12,
        leading=14,
        alignment=TA_CENTER,
        spaceBefore=6,
        spaceAfter=10,
    )
    ref_style = ParagraphStyle(
        "Ref",
        parent=body_style,
        fontSize=9.5,
        leading=12,
        leftIndent=10,
        firstLineIndent=-10,
        spaceAfter=4,
    )

    doc = SimpleDocTemplate(
        str(PDF_OUT),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
        title=source_text.splitlines()[0].lstrip("# ").strip(),
        author="OpenAI Codex",
    )
    max_image_width = doc.width
    max_image_height = 14 * cm

    story = []
    lines = source_text.splitlines()
    i = 0
    in_refs = False

    while i < len(lines):
        line = lines[i].rstrip()

        if not line:
            i += 1
            continue

        if line.startswith("# "):
            story.append(Paragraph(line[2:].strip(), title_style))
            i += 1
            continue

        if line.startswith("$$"):
            eq_lines = []
            stripped = line[2:].strip()
            if stripped:
                eq_lines.append(stripped)
            i += 1
            while i < len(lines):
                cur = lines[i].rstrip()
                if cur.endswith("$$"):
                    final = cur[:-2].strip()
                    if final:
                        eq_lines.append(final)
                    i += 1
                    break
                eq_lines.append(cur.strip())
                i += 1
            eq_text = clean_inline(" ".join(eq_lines))
            story.append(Paragraph(eq_text, equation_style))
            continue

        if line.startswith("## "):
            heading = line[3:].strip()
            in_refs = heading == "References"
            story.append(Spacer(1, 4))
            story.append(Paragraph(heading, h1_style))
            i += 1
            continue

        if line.startswith("### "):
            story.append(Paragraph(line[4:].strip(), h2_style))
            i += 1
            continue

        if line.startswith("!["):
            match = re.match(r"!\[(.*?)\]\((.*?)\)", line)
            if match:
                img_path = (SOURCE.parent / match.group(2)).resolve()
                if img_path.exists():
                    story.append(scale_image(img_path, max_image_width, max_image_height))
            i += 1
            continue

        if line.startswith("*Figure") and line.endswith("*"):
            story.append(Paragraph(clean_inline(line.strip("*")), caption_style))
            i += 1
            continue

        if line.startswith("|"):
            tbl, i = parse_table(lines, i)
            story.append(tbl)
            story.append(Spacer(1, 8))
            continue

        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(ListItem(Paragraph(clean_inline(lines[i][2:].strip()), body_style)))
                i += 1
            story.append(ListFlowable(items, bulletType="bullet", leftIndent=14))
            story.append(Spacer(1, 6))
            continue

        para_lines = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].rstrip()
            if not nxt:
                i += 1
                break
            if nxt.startswith(("#", "!", "|", "- ", "*Figure")):
                break
            para_lines.append(nxt)
            i += 1
        text = clean_inline(" ".join(s.strip() for s in para_lines))
        style = ref_style if in_refs else body_style
        story.append(Paragraph(text, style))

    def on_page(canvas, doc):
        canvas.setFont("Times-Roman", 9)
        canvas.setFillColor(colors.HexColor("#444444"))
        canvas.drawRightString(doc.pagesize[0] - 2 * cm, 1.2 * cm, str(canvas.getPageNumber()))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)


def main() -> None:
    source_text = SOURCE.read_text(encoding="utf-8")
    HTML_OUT.write_text(build_html(source_text), encoding="utf-8")
    build_pdf(source_text)
    print(f"Wrote {HTML_OUT}")
    print(f"Wrote {PDF_OUT}")


if __name__ == "__main__":
    main()
