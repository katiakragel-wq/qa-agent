import re
from pathlib import Path

text = Path("output_web_agent.md").read_text(encoding="utf-8")
match = re.search(r"```(?:typescript|ts)\n(.*?)```", text, re.S)
if not match:
    raise SystemExit("No TypeScript code block found in output_web_agent.md")

# The code arrives as one block; files are separated by lines like "// pages/LoginPage.ts"
parts = re.split(r"^// (\S+\.ts)\n", match.group(1), flags=re.M)
for name, body in zip(parts[1::2], parts[2::2]):
    path = Path("generated") / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.strip() + "\n", encoding="utf-8")
    print("written file", path)