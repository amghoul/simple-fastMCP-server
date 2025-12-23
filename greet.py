from fastmcp import FastMCP
import logging
import sys

# Silence all logging that isn't an actual Error
logging.getLogger("uvicorn.error").setLevel(logging.ERROR)
logging.getLogger("uvicorn.access").setLevel(logging.ERROR)

server = FastMCP("Demo")

@server.tool()
async def greet_user(name:str) -> str:
    """A tool that returns a greeting message"""
    return f"Hello {name}, how are you today?"

if __name__ == "__main__":
    # Ensure no print statements exist here
    server.run(transport="sse")