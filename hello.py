import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Name 3 risks to check when testing a login form."}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)