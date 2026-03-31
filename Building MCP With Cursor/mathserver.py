from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """_summary_
    Add two numbers together
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together"""

    return a * b

# The transport=stdio argument tells server to:
#Use Standard input/output (stdin/stdout) to receive and respond to tool function calls.

if __name__ == "__main__":
    mcp.run(transport="stdio")