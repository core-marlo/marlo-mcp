from uuid import UUID

from mcp.server.fastmcp import FastMCP

from marlo_mcp.client import MarloMCPClient
from marlo_mcp.client.schema import CreateEstimateSheetSchema, CreateVesselSchema, EstimateRequestSchema

mcp = FastMCP("marlo-mcp")


@mcp.tool(description="Get vessel all available vessels with minimal vessel details")
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


@mcp.tool(description="Search multiple ports")
async def search_ports(port_names: list[str]):
    """Search for multiple ports"""
    async with MarloMCPClient() as client:
        return await client.post("ports", data={"port_names": port_names})


@mcp.tool(description="Search cargos")
async def search_cargos(cargo_name: str):
    """Search for cargos"""
    async with MarloMCPClient() as client:
        return await client.post("cargos", data={"cargo_name": cargo_name})


@mcp.tool(description="Get all available charter specialists")
async def get_all_charter_specialists():
    """Get all available charter specialists"""
    async with MarloMCPClient() as client:
        return await client.get("charter-specialists")


@mcp.tool(description="Search charterer contacts")
async def search_charterer_contacts(charterer_name: str):
    """Search for charterer contacts"""
    async with MarloMCPClient() as client:
        return await client.post("charterer-contacts", data={"charterer_name": charterer_name})


@mcp.tool(
    description="Create an estimate sheet for a vessel to calculate the cost of a voyage. single estimate can have multiple estimates")
async def create_estimate_sheet(estimate_sheet: CreateEstimateSheetSchema):
    """create estimate sheet for a vessel to calculate the cost of a voyage. single estimate can have multiple estimates"""
    async with MarloMCPClient() as client:
        return await client.post("estimate-sheet", data=estimate_sheet.model_dump())


@mcp.tool(description="Calculate voyage estimate")
async def calculate_voyage_estimate(data: EstimateRequestSchema):
    """Calculate voyage estimate"""

    async with MarloMCPClient() as client:
        return await client.post("estimate", data=data.model_dump())


def main():
    mcp.run()


if __name__ == "__main__":
    main()
