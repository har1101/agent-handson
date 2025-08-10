# test_direct.py
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({
        "aws-knowledge": {
            "url": "https://knowledge-mcp.global.api.aws",
            "transport": "streamable_http",
            # 念のため Accept を明示
            "headers": {"Accept": "application/json, text/event-stream"},
        }
    })

    try:
        tools = await client.get_tools()
        print([t.name for t in tools])
    except Exception as e:
        import traceback; traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
