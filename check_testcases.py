import re
import sys

EXPECTED_COLUMNS = ["ID", "Title", "Preconditions", "Steps", "Expected result", "Type", "Covers"]
ALLOWED_TYPES = {"positive", "negative", "boundary"}
CRITERIA = ["AC1", "AC2", "AC3", "AC4", "AC5"]
MIN_CASES_PER_CRITERION = 2
MIN_EXTRA_CASES = 3

filename = sys.argv[1] if len(sys.argv) > 1 else "output_testcases.md"

with open(filename, encoding="utf-8") as f:
    lines = f.read().splitlines()

# 1. Extract the table rows
header = None
rows = []
for line in lines:
    line = line.strip()
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip("|").split("|")]
    if header is None:
        header = cells
        continue
    if all(set(c) <= set("-: ") for c in cells):  # separator row |---|---|
        continue
    if cells == header:  # repeated header row (the model sometimes writes a second table)
        continue
    rows.append(cells)

if header is None or "Type" not in header or "Covers" not in header:
    print("No table with Type and Covers columns found")
    sys.exit(1)

type_i = header.index("Type")
covers_i = header.index("Covers")

# 2. Check every test case
problems = []
if header != EXPECTED_COLUMNS:
    problems.append(f"Columns differ from the expected ones: {header}")

coverage = {ac: 0 for ac in CRITERIA}
extra = 0

for cells in rows:
    case_id = cells[0]
    if len(cells) != len(header):
        problems.append(f"{case_id}: expected {len(header)} columns, found {len(cells)}")
        continue

    case_type = cells[type_i]
    if case_type.lower() not in ALLOWED_TYPES:
        problems.append(f"{case_id}: Type is '{case_type}' (allowed: positive / negative / boundary)")

    covers = cells[covers_i]
    found = re.findall(r"AC\d+", covers.upper())
    if found:
        for ac in found:
            if ac in coverage:
                coverage[ac] += 1
            else:
                problems.append(f"{case_id}: unknown criterion {ac}")
    elif covers.lower() == "extra":
        extra += 1
    else:
        problems.append(f"{case_id}: Covers is '{covers}' (expected AC1-AC5 or extra)")

# 3. Report
print(f"File: {filename}")
print(f"Test cases: {len(rows)} (extra: {extra})")
print("Criteria coverage (by the Covers column):")
for ac in CRITERIA:
    mark = "  <-- NOT COVERED" if coverage[ac] == 0 else ""
    print(f"  {ac}: {coverage[ac]}{mark}")
print(f"Format problems: {len(problems)}")
for p in problems:
    print("  -", p)

passed = (
    not problems
    and all(coverage[ac] >= MIN_CASES_PER_CRITERION for ac in CRITERIA)
    and extra >= MIN_EXTRA_CASES
)
print("RESULT:", "PASS" if passed else "FAIL")
sys.exit(0 if passed else 1)