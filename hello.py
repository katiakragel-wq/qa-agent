import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Назови 3 риска, которые нужно проверить при тестировании формы логина."}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)