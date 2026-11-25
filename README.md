# qa-agent

A personal learning project: an AI agent that turns a Jira-style ticket into test cases, plus an automated checker and a small eval runner that measure how reliably the agent follows the required format and coverage rules.

Built in Python with the Claude API (tool use). Not a production tool.

## How it works

1. `agent.py` gives the model one tool, `read_ticket`. The model asks for the ticket, the code executes the tool and returns the text, and the loop continues until the model finishes.
2. The model writes test cases as a markdown table (ID, Title, Preconditions, Steps, Expected result, Type, Covers). `Covers` links each case to an acceptance criterion (AC1-AC5) or marks it `extra` if the ticket does not mention it.
3. `check_testcases.py` parses the table and checks:
   - the columns are correct and every row is complete;
   - `Type` is positive, negative or boundary;
   - every acceptance criterion has at least 2 cases;
   - at least 3 cases are marked `extra`.
4. `run_eval.py` runs the agent N times, saves every result to `runs/` and prints how many runs passed.

## Results

One ticket (`ticket.txt`, a login feature with 5 acceptance criteria), one prompt, 10 runs with `claude-haiku-5-5`:

- **9 of 10 runs passed** the checker.
- Run 9 failed for a real reason: the agent left out one cell in a table row.
- Run 10 first showed as a failure, but it was a false alarm in my own checker: the model split its answer into two tables, and the repeated header row was counted as a test case. I fixed the checker and re-scored all 10 saved runs with the same rules.

Things I noticed along the way:
- With the final prompt the number of test cases was fairly stable (16 to 18 across the 10 saved runs). Earlier prompt versions gave very different counts (from 11 to 39 in my first tests, which I did not save), so the wording of the prompt mattered more than run-to-run randomness.
- When I changed the prompt to require at least two cases per criterion, the agent produced only the minimum. Adding the explicit request for extra cases brought them back. Passing a check is not the same as good coverage.

## Limitations

- The checker validates **format and declared coverage only**. It cannot tell whether a test case is good or whether its expected result is correct. Some generated cases assume behaviour the ticket never states (for example, that the failed-attempt counter resets after a successful login), and a human has to review those.
- A single ticket and a single prompt: this is a small experiment, not a benchmark.
- The pass rules mirror the rules written in the prompt, so a pass mostly shows instruction-following.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...        # never commit the key
python agent.py testcases           # writes output_testcases.md
python check_testcases.py           # checks the last result
python run_eval.py 10               # 10 runs, results in runs/
```

`python agent.py summary` runs the first, simpler task (a short summary of the ticket).

## Next steps

- A small golden set of tickets with reference test cases, to measure accuracy and not only format.
- Playwright MCP for agent-driven exploration and test generation.
- Running the checks in CI.