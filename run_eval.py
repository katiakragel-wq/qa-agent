import shutil
import subprocess
import sys
from pathlib import Path

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
Path("runs").mkdir(exist_ok=True)

passed = 0
for i in range(1, N + 1):
    print(f"Run {i}/{N}...", flush=True)
    agent = subprocess.run(
        [sys.executable, "agent.py", "testcases"], capture_output=True, text=True
    )
    if agent.returncode != 0:
        print("  agent failed:", agent.stderr.strip()[-300:])
        continue

    saved = f"runs/run_{i:02d}.md"
    shutil.copy("output_testcases.md", saved)

    check = subprocess.run(
        [sys.executable, "check_testcases.py", saved], capture_output=True, text=True
    )
    ok = check.returncode == 0
    if ok:
        passed += 1
        print("   PASS")
    else:
        print("   FAIL")
        print(check.stdout)

print(f"Total: {passed} of {N} runs passed the check")