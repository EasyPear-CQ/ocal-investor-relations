# -*- coding: utf-8 -*-
"""Patch 2 (23 Oct 2026): facts page for the entity layer, LEI, ticker in every title (research file C). Kept for the record."""
import ast, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content.py')
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep('''    "wkn": "A42K21",''', '''    "wkn": "A42K21",
    "lei": "984500E70698C2C2AC97",''')

# Titles carry the brand string (research C, Part 2c)
rep('title="How OCAL works | The approval-first online car dealer",', 'title="How OCAL works | Approval-first online car dealer (TSXV: OCAL)",')
rep('title="OCAL Financial reports | Audited statements, MD&A and SEDAR+ filings",', 'title="OCAL Financial reports (TSXV: OCAL) | Audited statements, MD&A, SEDAR+",')
rep('title="OCAL operating metrics | Vehicles funded, gross profit per vehicle, margin",', 'title="OCAL operating metrics (TSXV: OCAL) | Vehicles funded, gross profit per vehicle",')
rep('title="OCAL investor events | AGM, reporting dates and conferences",', 'title="OCAL Financial events (TSXV: OCAL) | AGM, reporting dates, conferences",')
rep('title="OCAL investor presentation, fact sheet and brief | Dated documents",', 'title="OCAL Financial investor presentation and fact sheet (TSXV: OCAL)",')
rep('title="OCAL corporate governance | Board, committees, charters and policies",', 'title="OCAL Financial governance (TSXV: OCAL) | Board, committees, policies",')
rep('title="OCAL leadership | Mehdi Moghareh, Matthew Friesen and the team",', 'title="OCAL Financial leadership (TSXV: OCAL) | Mehdi Moghareh, Matthew Friesen",')
rep('title="OCAL investor FAQ | The hard questions, answered first",', 'title="OCAL Financial investor FAQ (TSXV: OCAL) | The hard questions first",')
rep('title="Contact OCAL investor relations | Book a call with the founders",', 'title="Contact OCAL Financial investor relations (TSXV: OCAL)",')
rep('title="OCAL email alerts | News releases and results by email",', 'title="OCAL Financial email alerts (TSXV: OCAL) | Releases by email",')
rep('title="OCAL Financial investor fact sheet | One page, October 2026",', 'title="OCAL Financial fact sheet (TSXV: OCAL) | One page, October 2026",')

# Facts page: the entity page AI engines and data vendors read (research C, Part 2b and 2c)
facts = '''
# ------------------------------------------------------------------ FACTS (entity page)
page(
    slug="/facts/",
    nav_label="Company facts",
    title="OCAL Financial facts (TSXV: OCAL) | Symbols, address, officers, auditor",
    description="Reference facts for OCAL Financial Inc.: legal name, TSXV and Frankfurt symbols, ISIN, CUSIP, LEI, head office, officers and directors, transfer agent, auditor, counsel, fiscal year end and listing date. Updated 23 October 2026.",
    hero={
        "kicker": "COMPANY FACTS",
        "h1": "The facts, <em>in one place.</em>",
        "sub": "The reference page for data vendors, journalists, AI assistants and anyone checking a detail. Same facts as the structured data on every page. No marketing.",
        "ctas": [],
    },
    blocks=[
        ("table", ["Fact", "Value"], [
            ["Legal name", "OCAL Financial Inc."],
            ["Former name", "Ronin Ventures Corp. (capital pool company; qualifying transaction completed 15 July 2026)"],
            ["Operating subsidiary", "1301756 B.C. Ltd., incorporated 23 April 2021, wholly owned"],
            ["What the company does", "Approval-first online automotive dealership and vehicle-finance platform. The customer is approved by a lender first; OCAL, the licensed motor dealer of record, then sources the vehicle through OPENLANE, its exclusive auction and sourcing channel, and delivers it. Zero standing inventory; no consumer loans held; not a broker."],
            ["Industry", "Automotive retail (online vehicle sales) and vehicle finance arrangement"],
            ["Stock exchange listings", "TSX Venture Exchange: OCAL (Tier 2), trading since 21 July 2026. Frankfurt Stock Exchange: JC3, since 25 August 2026."],
            ["ISIN", SITE["isin"]],
            ["CUSIP", SITE["cusip"]],
            ["WKN", SITE["wkn"]],
            ["LEI", SITE["lei"] + " [[Confirm the registered address on GLEIF matches Suite 500, 885 Dunsmuir Street; the register shows a West Georgia Street address.]]"],
            ["Shares outstanding", "36,667,803 (as at " + SITE["facts_date"] + ")"],
            ["Fiscal year end", "31 August"],
            ["Head office", SITE["address"]],
            ["Edmonton hub", SITE["edmonton"]],
            ["Telephone", SITE["phone"]],
            ["Investor relations email", SITE["email"]],
            ["Websites", "Investors: investors.ocal.ca. Customers: ocalfinancial.ca."],
            ["Chief Executive Officer", "Mehdi Moghareh (Co-Founder, Director)"],
            ["Executive Chairman", "Matthew Friesen (Co-Founder, Director)"],
            ["Chief Financial Officer", "Terence Lee, CPA"],
            ["Independent directors", "Michael Stier (Chair of the Audit Committee and of the Compensation, Governance and Nominating Committee); Robert Birmingham"],
            ["Auditor", "DMCL LLP, Vancouver"],
            ["Transfer agent and registrar", "Endeavor Trust Corporation, Vancouver"],
            ["Legal counsel", "Lawson Lundell LLP, Vancouver"],
            ["Investor relations firm", "Signal Capital Advisors Inc., Toronto (Shushu Feng)"],
            ["Market maker", "Integral Wealth Securities Limited"],
            ["Newswire", "Newsfile Corp."],
            ["Dealer licences", "British Columbia: OCAL Financial Inc., licensed motor dealer, VSA D50207. Alberta: AMVIC-licensed business, AMVIC B2036050."],
            ["Operating since", "April 2021"],
            ["Employees", "About 30 people plus a part-time driver network (management information)"],
            ["Continuous disclosure", "SEDAR+ (www.sedarplus.ca), issuer profile OCAL Financial Inc."],
            ["Last updated", SITE["facts_date"]],
        ], "Each line is traceable to a filing, a news release or a public register. Corrections to investors@ocal.ca."),
        ("h2", "Standard description for third parties"),
        ("p", "**Short (one line).** Virtual automotive dealership and vehicle-finance platform, licensed in British Columbia and Alberta."),
        ("p", "**Standard (for data vendors).** OCAL Financial Inc. is a Vancouver-based, asset-light online automotive dealership and vehicle-finance platform. Operating remotely and licensed in British Columbia and Alberta, OCAL takes customers from application to lender approval, vehicle matching, digital contracting and delivery. It sources each vehicle only after approval, through OPENLANE Canada, its exclusive auction and sourcing channel, and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans or take credit-default risk."),
        ("p", "Media and data vendors may use either description without further permission. Logos are in the [media kit](/presentations/)."),
    ],
)
'''
rep('''# ------------------------------------------------------------------ LEGAL''', facts + '''
# ------------------------------------------------------------------ LEGAL''')

# footer link to facts
rep('''("Company", [("Why OCAL", "/why-ocal/"), ("How it works", "/how-it-works/"), ("Leadership", "/leadership/"), ("Governance", "/governance/"), ("Fact sheet", "/fact-sheet/")]),''',
    '''("Company", [("Why OCAL", "/why-ocal/"), ("How it works", "/how-it-works/"), ("Leadership", "/leadership/"), ("Governance", "/governance/"), ("Company facts", "/facts/"), ("Fact sheet", "/fact-sheet/")]),''')

open(p, 'w', encoding='utf-8').write(s)
ast.parse(s)
print('patched 2; dashes:', s.count('—') + s.count('–'))
