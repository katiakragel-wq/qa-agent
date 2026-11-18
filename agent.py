import anthropic

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

messages = [
    {"role": "user", "content": "Прочитай тикет из файла ticket.txt и коротко скажи, о чём он."}
]

for step in range(5):
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1000,
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

for block in response.content:
    if block.type == "text":
        print(block.text)