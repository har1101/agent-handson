# test_remote.py
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({
        "aws-knowledge": {
            "command": "npx",
            "args": ["mcp-remote", "https://knowledge-mcp.global.api.aws"],
            "transport": "stdio",
        }
    })

    try:
        tools = await client.get_tools()
        print([t.name for t in tools])
    except Exception as e:
        import traceback; traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
