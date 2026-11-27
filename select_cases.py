import sys

SOURCE = sys.argv[1] if len(sys.argv) > 1 else "output_testcases.md"
TARGET = "selected_cases.md"
MAX_CASES = 10

with open(SOURCE, encoding="utf-8") as f:
    lines = [line.strip() for line in f.read().splitlines()]

# Read the table rows (same rules as in check_testcases.py)
header = None
rows = []
for line in lines:
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip("|").split("|")]
    if header is None:
        header = cells
        continue
    if all(set(c) <= set("-: ") for c in cells):  # separator row
        continue
    if cells == header:  # repeated header row
        continue
    rows.append(cells)

if header is None or "Covers" not in header:
    raise SystemExit("No table with a Covers column found in " + SOURCE)

# Selection rule: cases that come from the ticket (Covers is not 'extra'), first MAX_CASES
covers_i = header.index("Covers")
selected = [
    r for r in rows if len(r) == len(header) and r[covers_i].lower() != "extra"
][:MAX_CASES]
selected_ids = {r[0] for r in selected}
not_selected = [r[0] for r in rows if r[0] not in selected_ids]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write("| " + " | ".join(header) + " |\n")
    f.write("|" + "---|" * len(header) + "\n")
    for r in selected:
        f.write("| " + " | ".join(r) + " |\n")

print(f"Selected {len(selected)} of {len(rows)} cases -> {TARGET}")
print("Selected:    ", ", ".join(r[0] for r in selected))
print("Not selected:", ", ".join(not_selected) or "none")