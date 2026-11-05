# -*- coding: utf-8 -*-
"""Patch 8 (26 Oct 2026, Matthew): the metrics block is per vehicle again, built from the audited FY2025 and FY2024
figures. Unit counts are not in the statements, so they are derived (FY2025 vehicle sales $5,630,980 at about $29,000
per vehicle gives about 195; FY2024 at the same revenue per vehicle gives about 165) and flagged for Terence.
The audited totals table moves to the Operating metrics page under the per-vehicle block. Kept for the record."""
import os, ast
HERE = os.path.dirname(os.path.abspath(__file__))

p = os.path.join(HERE, "build_site.py"); s = open(p, encoding="utf-8").read()
old = s[s.index("def kpi_table(depth, slug):"):s.index("def deals_chart():")]
new = '''def kpi_table(depth, slug):
    # FY2025 audited: revenue 6,480,254 (vehicle sales 5,630,980; F&I 849,274); gross profit 810,751 (vehicle 109,024; F&I 701,727);
    # write-downs 353,094. Units derived: about 195 (FY2025), about 165 (FY2024 at the same revenue per vehicle). Terence confirms.
    rows = [
        ["Vehicles funded and delivered", "about 195 [[Terence: FY2025 count from the ledger]]", "about 165 [[Terence: FY2024 count]]", ""],
        ["Average vehicle selling price", "about $28,900", "[[FY2024 vehicle sales divided by the count]]", ""],
        ["Deal gross profit per vehicle (before vehicle write-downs), of which vehicle margin and finance, insurance and protection income", "about $5,970 ($2,370 + $3,600)", "[[needs FY2024 write-downs and split]]", ""],
        ["Gross profit per vehicle (IFRS basis)", "about $4,160 ($560 + $3,600)", "about $3,700", "+12%"],
        ["Revenue per vehicle", "about $33,200", "about $33,200 (assumed equal)", ""],
        ["Gross margin", "12.5%", "11.2%", "+1.3 pts"],
    ]
    return render_table(["Per vehicle, fiscal year ended 31 August", "FY2025 (audited basis)", "FY2024 (audited basis)", "Change"], rows,
                        "Dollar totals are from the audited financial statements for the year ended 31 August 2025 (DMCL LLP): revenue $6,480,254 (vehicle sales $5,630,980, finance, insurance and other $849,274), gross profit $810,751 (vehicle $109,024, finance and protection $701,727), vehicle write-downs in cost of sales $353,094; FY2024 revenue $5,454,893 and gross profit $610,787. Vehicle counts are management estimates derived from vehicle sales revenue at about $29,000 per vehicle and are confirmed from the ledger before go-live; per-vehicle figures change with the confirmed counts. Deal gross profit per vehicle is a non-IFRS measure (gross profit plus vehicle write-downs, divided by vehicles). From the October 2026 operating update the same block is published monthly.", slug, depth)

def audited_table(depth, slug):
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
                        "From the audited financial statements for the year ended 31 August 2025 and their FY2024 comparatives; the FY2024 revenue mix and gross profit split are in the statements on SEDAR+. Gross profit before vehicle write-downs is a non-IFRS measure.", slug, depth)

'''
s = s.replace(old, new)
s = s.replace('''            elif w == "kpi-table": out.append(kpi_table(depth, slug))''', '''            elif w == "kpi-table": out.append(kpi_table(depth, slug))
            elif w == "audited-table": out.append(audited_table(depth, slug))''')
open(p, "w", encoding="utf-8").write(s)

p = os.path.join(HERE, "content.py"); s = open(p, encoding="utf-8").read()
def rep(a, b):
    global s
    assert a in s, a[:80]
    s = s.replace(a, b, 1)
rep('''        ("h2", "The economics, from the audited statements"),
        ("p", "Investors used to spend the first half hour of every call rebuilding OCAL's gross margin from scraps. Here are the audited fiscal 2025 figures beside fiscal 2024: revenue up 18.8 percent, gross profit up 32.7 percent, gross margin up to 12.5 percent, and $1.16 million of gross profit before vehicle write-downs. From the October 2026 operating update the same block is published every month with per-vehicle figures under fixed definitions."),''',
    '''        ("h2", "The per-vehicle economics, from the audited statements"),
        ("p", "Investors used to spend the first half hour of every call rebuilding OCAL's gross margin from scraps. Here is the per-vehicle picture built from the audited fiscal 2025 statements, beside fiscal 2024: what a vehicle sells for, what each one earns on the deal basis and on the IFRS basis, and the margin. From the October 2026 operating update the same block is published every month under fixed definitions."),''')
rep('''        ("h2", "Audited annual results"),
        ("widget", "kpi-table"),
        ("h2", "Monthly history"),''',
    '''        ("h2", "Per vehicle, from the audited statements"),
        ("widget", "kpi-table"),
        ("h2", "The audited totals behind it"),
        ("widget", "audited-table"),
        ("h2", "Monthly history"),''')
open(p, "w", encoding="utf-8").write(s); ast.parse(s)
print("patched 8")
