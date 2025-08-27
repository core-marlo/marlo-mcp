from uuid import UUID

from mcp.server.fastmcp import FastMCP

from marlo_mcp.client import MarloMCPClient
from marlo_mcp.client.schema import BillQueryParams, CreateEstimateSheetSchema, CreateVesselSchema, EstimateRequestSchema, ListInvoiceParams, VoyageProfitAndLoss

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


# @mcp.tool(description="create a new vessel")
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


@mcp.tool(description="Get all voyages")
async def get_all_voyages():
    """Get all voyages"""
    async with MarloMCPClient() as client:
        return await client.get("voyages")


@mcp.tool(description="Get voyage details")
async def get_voyage_details(voyage_id: UUID):
    """Get details of a specific voyage"""
    async with MarloMCPClient() as client:
        return await client.get(f"voyage/{voyage_id}")


@mcp.tool(description="Get voyage profit and loss")
async def get_voyage_profit_and_loss(data: VoyageProfitAndLoss):
    """Get profit and loss of a specific voyage"""
    async with MarloMCPClient() as client:
        return await client.post(f"voyage/{data.voyage_id}/profit-and-loss", data=data.model_dump())


@mcp.tool(description="Get all estimates sheet")
async def get_all_estimates_sheet():
    """Get all estimates sheet"""
    async with MarloMCPClient() as client: 
        return await client.get("estimate-sheets")


@mcp.tool(description="get details of a specific estimate sheet")
async def get_estimate_sheet_details(estimate_sheet_id: UUID):
    """Get details of a specific estimate sheet"""
    async with MarloMCPClient() as client: 
        return await client.get(f"estimate-sheet/{estimate_sheet_id}")


@mcp.tool(description="Get all cargo books")
async def get_all_cargo_books():
    """Get all cargo books"""
    async with MarloMCPClient() as client:
        return await client.get("cargo-books")


@mcp.tool(description="Get cargo book details")
async def get_cargo_book_details(cargo_book_id: UUID):
    """Get details of a specific cargo book"""
    async with MarloMCPClient() as client:
        return await client.get(f"cargo-book/{cargo_book_id}")


@mcp.tool(description="list all vessel fixtures")
async def list_all_vessel_fixtures():
    """List all vessel fixtures"""
    async with MarloMCPClient() as client:
        return await client.get("vessel-fixtures")


@mcp.tool(description="get details of a specific vessel fixture")
async def get_vessel_fixture_details(vessel_fixture_id: UUID):
    """Get details of a specific vessel fixture"""
    async with MarloMCPClient() as client:
        return await client.get(f"vessel-fixture/{vessel_fixture_id}")


@mcp.tool(description="get voyage contacts")
async def get_voyage_contacts(voyage_id: UUID):
    """Get voyage contacts"""
    async with MarloMCPClient() as client:
        return await client.get(f"voyage/{voyage_id}/contacts")


@mcp.tool(description="Get financial details (bills, invoices, payments, etc.) for voyage contacts")
async def get_voyage_contacts_financial_details(voyage_id: UUID, contact_id: str, contact_type: str):
    """Get financial details (bills, invoices, payments, etc.) for voyage contacts"""
    async with MarloMCPClient() as client:
        return await client.get(f"voyage/{voyage_id}/contact/{contact_id}/finance?contact_type={contact_type}")


@mcp.tool(description="get contacts for a vessel fixture")
async def get_vessel_fixture_contacts(vessel_fixture_id: UUID):
    """Get contacts for a vessel fixture"""
    async with MarloMCPClient() as client:
        return await client.get(f"time-chartered/{vessel_fixture_id}/contacts")


@mcp.tool(description="Get vessel fixture contacts financial details (bills, invoices, payments, etc.)")
async def get_vessel_fixture_contacts_financial_details(vessel_fixture_id: UUID, contact_id: str, contact_type: str):
    """Get financial details (bills, invoices, payments, etc.) for vessel fixture contacts"""
    async with MarloMCPClient() as client:
        return await client.get(f"time-chartered/{vessel_fixture_id}/contact/{contact_id}/finance?contact_type={contact_type}")


@mcp.tool(description="Get a invoice details")
async def get_invoice_details(invoice_id: str):
    """Get a invoice details"""
    async with MarloMCPClient() as client:
        return await client.get(f"invoice/{invoice_id}")


@mcp.tool(description="Get a bill details")
async def get_bill_details(bill_id: str):
    """Get a bill details"""
    async with MarloMCPClient() as client:
        return await client.get(f"bill/{bill_id}")


@mcp.tool(description="voyage port disbursements")
async def voyage_port_disbursements(voyage_id: UUID):
    """Get voyage port disbursements"""
    async with MarloMCPClient() as client:
        return await client.get(f"voyage/{voyage_id}/port-disbursements")


@mcp.tool(description="Get voyage laytime")
async def get_voyage_laytime(voyage_id: UUID):
    """Get voyage laytime"""
    async with MarloMCPClient() as client:
        return await client.get(f"laytime/{voyage_id}")


@mcp.tool(description="list all customers")
async def list_all_customers(page: int = 1, per_page: int = 100, search: str = None):
    """List all customers"""
    async with MarloMCPClient() as client:
        return await client.get("customers", params={"page": page, "per_page": per_page, "search": search})


@mcp.tool(description="list all vendors")
async def list_all_vendors(page: int = 1, per_page: int = 100, search: str = None):
    """List all vendors"""
    async with MarloMCPClient() as client:
        return await client.get("vendors", params={"page": page, "per_page": per_page, "search": search})


@mcp.tool(description="list all lendors")
async def list_all_lendors(page: int = 1, per_page: int = 100, search: str = None):
    """List all lendors"""
    async with MarloMCPClient() as client:
        return await client.get("lendors", params={"page": page, "per_page": per_page, "search": search})


@mcp.tool(description="get customer details")
async def get_customer_details(customer_id: str):
    """Get customer details"""
    async with MarloMCPClient() as client:
        return await client.get(f"customer/{customer_id}")


@mcp.tool(description="get vendor details")
async def get_vendor_details(vendor_id: str):
    """Get vendor details"""
    async with MarloMCPClient() as client:
        return await client.get(f"vendor/{vendor_id}")


@mcp.tool(description="list all bills")
async def list_all_bills(data: BillQueryParams):
    """List all bills"""
    async with MarloMCPClient() as client:
        return await client.get("bills", params=data.model_dump())


@mcp.tool(description="list all invoices")
async def list_all_invoices(data: ListInvoiceParams):
    """List all invoices"""
    async with MarloMCPClient() as client:
        return await client.get("invoices", params=data.model_dump())


@mcp.tool(description="get journal entries")
async def get_journal_entries():
    """Get journal entries"""
    async with MarloMCPClient() as client:
        return await client.get("journal-entries")


@mcp.tool(description="list all vendor credits")
async def list_all_vendor_credits():
    """List all vendor credits"""
    async with MarloMCPClient() as client:
        return await client.get("vendor-credit-notes")


@mcp.tool(description="get vendor credit details")
async def get_vendor_credit_details(vendor_credit_id: str):
    """Get vendor credit details"""
    async with MarloMCPClient() as client:
        return await client.get(f"vendor-credit-notes/{vendor_credit_id}")


@mcp.tool(description="list all credit notes")
async def list_all_credit_notes():
    """List all credit notes"""
    async with MarloMCPClient() as client:
        return await client.get("credit-notes")


@mcp.tool(description="get credit note details")
async def get_credit_note_details(credit_note_id: str):
    """Get credit note details"""
    async with MarloMCPClient() as client:
        return await client.get(f"credit-notes/{credit_note_id}")


@mcp.tool(description="list all exteral loans")
async def list_all_external_loans():
    """List all external loans"""
    async with MarloMCPClient() as client:
        return await client.get("external-loans")


@mcp.tool(description="get external loan details")
async def get_external_loan_details(application_id: str):
    """Get external loan details"""
    async with MarloMCPClient() as client:
        return await client.get(f"external-loans/{application_id}")


@mcp.tool(description="list all marlo loans")
async def list_all_marlo_loans():
    """List all marlo loans"""
    async with MarloMCPClient() as client:
        return await client.get("loans")


@mcp.tool(description="get marlo loan details")
async def get_marlo_loan_details(application_id: str):
    """Get marlo loan details"""
    async with MarloMCPClient() as client:
        return await client.get(f"loans/{application_id}")



def main():
    mcp.run()


if __name__ == "__main__":
    main()
