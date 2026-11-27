import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server = StdioServerParameters(
    command="npx",
    args=["-y", "@playwright/mcp@0.0.85", "--browser", "chromium",
          "--headless", "--no-sandbox", "--isolated"],
)


async def main():
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.list_tools()
            print("Tools:", len(result.tools))
            for tool in result.tools:
                print("-", tool.name)


asyncio.run(main())