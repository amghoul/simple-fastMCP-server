import asyncio
from mcp.client.sse import sse_client
from mcp.client.session import ClientSession
import sys

async def run():
    # Replace with your actual cloud URL
    url = "https://moaning-scarlet-gecko.fastmcp.app/sse"
    async with sse_client(url) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            # This bridges the cloud SSE to Claude's local STDIO
            print("Connected to cloud MCP", file=sys.stderr)
            # Logic to keep the connection open
            while True:
                await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())