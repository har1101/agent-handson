# test_fs_only.py
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({
        "file-system": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                # ★ 実在するローカルパスに置き換え（例では chapter4 直下）
                "./"
            ],
            "transport": "stdio",
        }
    })

    tools = await client.get_tools()
    print("Loaded tools:", [t.name for t in tools])

if __name__ == "__main__":
    asyncio.run(main())