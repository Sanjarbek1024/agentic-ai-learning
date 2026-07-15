from mcp.server.fastmcp import FastMCP

mcp = FastMCP('demo')

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


if __name__ == '__main__':
    mcp.run(transport='stdio')