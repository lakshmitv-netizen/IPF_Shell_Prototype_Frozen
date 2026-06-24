#!/usr/bin/env python3
"""Optional patch: rename "Measure category" -> "Measure subsets" and show all
measures of the selected subset(s) by default (Configure-unchecking hides them).

Applies to the cp-app and cp-grid-app bundles in this snapshot. NOT applied by
default. Run from the repo root:

    python3 patches/measure_subsets.py
"""
import os

FILES = [
    "docs/cp-app/static/js/main.7c479505.js",
    "docs/cp-grid-app/static/js/main.7c479505.js",
]

EDITS = [
    # --- rename ---
    ('{marginBottom:0},children:"Measure category"})',
     '{marginBottom:0},children:"Measure subsets"})'),
    ('" Categor").concat(1!==ht()?"ies":"y"," Selected")',
     '" Subset").concat(1!==ht()?"s":""," Selected")'),
    (':"Select Measure Category"}),(0,qt.jsx)("svg"',
     ':"Select Measure Subset"}),(0,qt.jsx)("svg"'),
    ('"aria-label":"Measure category options"',
     '"aria-label":"Measure subset options"'),
    ('children:"Select measure category:"}',
     'children:"Select measure subset:"}'),
    ('multiple categories, select a category to change its context.',
     'multiple subsets, select a subset to change its context.'),
    ('"All measure categories":0===t.length?"No measure categories"',
     '"All measure subsets":0===t.length?"No measure subsets"'),
    # --- behavior: don't narrow to config selectedMeasureIds; show all of subset ---
    ('a.length>0&&(e=a,i=!0)', 'a.length>0&&(i=!1)'),
    ('if(R(e),E(e),i)P(new Set(o));else{const e=new Set(Array.from(No).filter(e=>o.includes(e)));P(e.size>0?e:new Set(o))}',
     'R(e),E(e),P(new Set(o))'),
]


def main():
    for f in FILES:
        if not os.path.exists(f):
            print("SKIP (missing):", f)
            continue
        s = open(f, encoding="utf-8").read()
        for old, new in EDITS:
            n = s.count(old)
            assert n == 1, f"{f}: expected 1 occurrence, found {n} for: {old[:60]!r}"
            s = s.replace(old, new)
        open(f, "w", encoding="utf-8").write(s)
        print("patched", f)
    print("done")


if __name__ == "__main__":
    main()
