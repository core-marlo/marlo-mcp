from uuid import UUID
from mcp.server.fastmcp import FastMCP
from marlo_mcp import MarloMCPClient

mcp = FastMCP("marlo-mcp")

@mcp.tool(description="Get vessel all available vessels")
async def get_vessels():
    """Get all available vessels"""
    async with MarloMCPClient() as client:
        return await client.get("vessels")

@mcp.tool(description="Get vessel details")
async def get_vessel_details(vessel_id: UUID):
    """Get details of a specific vessel"""
    async with MarloMCPClient() as client:
        return await client.get(f"vessel/{vessel_id}")