# -*- coding: utf-8 -*-
"""Patch 7 (26 Oct 2026, Matthew): the metrics block on the home page and the Operating metrics page shows the
audited fiscal 2025 and fiscal 2024 figures, same table, instead of the October and September placeholders.
Monthly figures start with the October operating update and go into the history table. Kept for the record."""
import os, ast
HERE = os.path.dirname(os.path.abspath(__file__))

p = os.path.join(HERE, "build_site.py"); s = open(p, encoding="utf-8").read()
old = s[s.index("def kpi_table(depth, slug):"):s.index("def deals_chart():")]
new = '''def kpi_table(depth, slug):
    rows = [
        ["Revenue", "$6,480,254", "$5,454,893", "+18.8%"],
        ["Of which vehicle sales", "$5,630,980 (86.9%)", "", ""],
        ["Of which finance, insurance and other", "$849,274 (13.1%)", "", ""],
        ["Gross profit", "$810,751", "$610,787", "+32.7%"],
        ["Of which vehicle margin", "$109,024", "", ""],
        ["Of which finance, insurance and protection income", "$701,727", "", ""],
        ["Gross margin", "12.5%", "11.2%", "+1.3 pts"],
        ["Vehicle write-downs included in cost of sales", "$353,094", "", ""],
        ["Gross profit before vehicle write-downs (deal basis)", "$1,163,845 (18.0% of revenue)", "", ""],
        ["Operating loss", "($303,444)", "", ""],
        ["Net loss", "($322,090)", "", ""],
    ]
    return render_table(["Fiscal year ended 31 August", "FY2025 (audited)", "FY2024 (audited)", "Change"], rows,
                        "From the audited financial statements for the year ended 31 August 2025 (DMCL LLP) and their FY2024 comparatives; the FY2024 revenue mix and gross profit split are shown in the statements on SEDAR+. Gross profit before vehicle write-downs is a non-IFRS measure, calculated as audited gross profit plus the vehicle write-downs in cost of sales. From the October 2026 operating update the same block is published monthly with per-vehicle figures.", slug, depth)

'''
s = s.replace(old, new); open(p, "w", encoding="utf-8").write(s)

p = os.path.join(HERE, "content.py"); s = open(p, encoding="utf-8").read()
def rep(a, b):
    global s
    assert a in s, a[:80]
    s = s.replace(a, b, 1)
rep('''        ("h2", "The per-vehicle economics, published every period"),
        ("p", "Investors used to spend the first half hour of every call rebuilding OCAL's gross margin from scraps. From the October 2026 operating update, the numbers that describe the business are published every month with the same definitions every time and kept here: vehicles funded and delivered, average selling price, gross profit per vehicle on both the deal basis and the IFRS basis, and gross margin. Historical only, unaudited, read with the filed statements."),''',
    '''        ("h2", "The economics, from the audited statements"),
        ("p", "Investors used to spend the first half hour of every call rebuilding OCAL's gross margin from scraps. Here are the audited fiscal 2025 figures beside fiscal 2024: revenue up 18.8 percent, gross profit up 32.7 percent, gross margin up to 12.5 percent, and $1.16 million of gross profit before vehicle write-downs. From the October 2026 operating update the same block is published every month with per-vehicle figures under fixed definitions."),''')
rep('''        ("h2", "Latest period"),
        ("widget", "kpi-table"),
        ("h2", "History"),''',
    '''        ("h2", "Audited annual results"),
        ("widget", "kpi-table"),
        ("h2", "Monthly history"),''')
open(p, "w", encoding="utf-8").write(s); ast.parse(s)
print("patched 7")
