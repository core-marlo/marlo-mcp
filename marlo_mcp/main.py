from uuid import UUID
from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from marlo_mcp.client import MarloMCPClient
from marlo_mcp.client.schema import CreateVesselSchema
from mcp.server.elicitation import (
    AcceptedElicitation,
    DeclinedElicitation,
    CancelledElicitation,
)

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
    
@mcp.tool(description="create a new vessel")
async def create_vessel(vessel: CreateVesselSchema):
    """Create a new vessel"""
    async with MarloMCPClient() as client:
        return await client.post("vessel", data=vessel.model_dump())

def main():
    import asyncio
    asyncio.run(mcp.run())

if __name__ == "__main__":
    main()