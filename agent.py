import anthropic
import sys
client = anthropic.Anthropic()


def read_ticket(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


tools = [
    {
        "name": "read_ticket",
        "description": "Reads a ticket from a text file and returns its text.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the ticket file, for example ticket.txt",
                }
            },
            "required": ["path"],
        },
    }
]
TASKS = {
    "summary": "Прочитай тикет из файла ticket.txt и коротко скажи, о чём он.",
    "testcases": (
        "Read the ticket from ticket.txt. Number its acceptance criteria AC1, AC2, ... "
        "in the order they appear in the ticket. Then write test cases for it as a markdown table "
        "with exactly these columns: ID, Title, Preconditions, Steps, Expected result, Type, Covers.\n"
        "Rules:\n"
        "- Type must be exactly one of: positive, negative, boundary. Never write 'extra' in Type.\n"
        "- Covers must be the acceptance criterion the case checks (AC1 to AC5), "
        "or 'extra' if the case checks something the ticket does not mention.\n"
        "- Every acceptance criterion must have at least two test cases.\n"
        "- Also add at least three cases with Covers = extra for edge cases the ticket does not mention (Type must still be positive, negative or boundary).\n"
        "Write in English."
    ),
}
task_name = sys.argv[1] if len(sys.argv) > 1 else "testcases"
messages = [{"role": "user", "content": TASKS[task_name]}]
for step in range(5):
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=8000,
        tools=tools,
        messages=messages,
    )
    messages.append({"role": "assistant", "content": response.content})

    if response.stop_reason != "tool_use":
        break

    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            print("вызов инструмента:", block.name, block.input)
            if block.name == "read_ticket":
                result = read_ticket(**block.input)
            else:
                result = "Unknown tool"
            tool_results.append(
                {"type": "tool_result", "tool_use_id": block.id, "content": result}
            )
    messages.append({"role": "user", "content": tool_results})

output_text = "\n".join(b.text for b in response.content if b.type == "text")
filename = f"output_{task_name}.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(output_text)
print(f"Saved to {filename}")
print("stop_reason:", response.stop_reason, "| output tokens:", response.usage.output_tokens)