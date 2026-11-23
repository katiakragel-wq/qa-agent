import re
import sys

EXPECTED_COLUMNS = ["ID", "Title", "Preconditions", "Steps", "Expected result", "Type", "Covers"]
ALLOWED_TYPES = {"positive", "negative", "boundary"}
CRITERIA = ["AC1", "AC2", "AC3", "AC4", "AC5"]

filename = sys.argv[1] if len(sys.argv) > 1 else "output_testcases.md"

with open(filename, encoding="utf-8") as f:
    lines = f.read().splitlines()

# 1. Достаём строки таблицы
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
    if all(set(c) <= set("-: ") for c in cells):  # строка-разделитель |---|---|
        continue
    rows.append(cells)

if header is None or "Type" not in header or "Covers" not in header:
    print("Таблица с колонками Type и Covers не найдена")
    sys.exit(1)

type_i = header.index("Type")
covers_i = header.index("Covers")

# 2. Проверяем каждый кейс
problems = []
if header != EXPECTED_COLUMNS:
    problems.append(f"Колонки не совпадают с ожидаемыми: {header}")

coverage = {ac: 0 for ac in CRITERIA}
extra = 0

for cells in rows:
    case_id = cells[0]
    if len(cells) != len(header):
        problems.append(f"{case_id}: ожидалось колонок {len(header)}, найдено {len(cells)}")
        continue

    case_type = cells[type_i]
    if case_type.lower() not in ALLOWED_TYPES:
        problems.append(f"{case_id}: в Type стоит '{case_type}' (допустимо: positive / negative / boundary)")

    covers = cells[covers_i]
    found = re.findall(r"AC\d+", covers.upper())
    if found:
        for ac in found:
            if ac in coverage:
                coverage[ac] += 1
            else:
                problems.append(f"{case_id}: неизвестный критерий {ac}")
    elif covers.lower() == "extra":
        extra += 1
    else:
        problems.append(f"{case_id}: в Covers стоит '{covers}' (нужен AC1-AC5 или extra)")

# 3. Отчёт
print(f"Файл: {filename}")
print(f"Кейсов: {len(rows)} (из них extra: {extra})")
print("Покрытие критериев (по колонке Covers):")
for ac in CRITERIA:
    mark = "  <-- НЕ ПОКРЫТ" if coverage[ac] == 0 else ""
    print(f"  {ac}: {coverage[ac]}{mark}")
print(f"Проблем с форматом: {len(problems)}")
for p in problems:
    print("  -", p)