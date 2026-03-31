from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the weather for a given city"""
    return f"It is always raining in the california"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")