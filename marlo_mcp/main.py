from typing import Optional
from uuid import UUID
from typing import Optional

from mcp.server.fastmcp import FastMCP

from marlo_mcp.client import MarloMCPClient
from marlo_mcp.client.schema import BillQueryParams, CreateVesselSchema, ListInvoiceParams, SearchInputData, VoyageProfitAndLoss, VesselValuationRequestSchema

mcp = FastMCP("marlo-mcp")


@mcp.tool(description="Get vessel all available vessels with minimal vessel details")
async def get_vessels():
    """Get all available vessels"""
    async with MarloMCPClient() as client:
        return await client.get("vessels")


@mcp.tool(description="Get all available fleets")
async def get_fleets():
    """Get all available fleets"""
    async with MarloMCPClient() as client:
        return await client.get("fleets")


@mcp.tool(description="Get fleet details")
async def get_fleet_details(fleet_id: UUID):
    """Get details of a specific fleet"""
    async with MarloMCPClient() as client:
        return await client.get(f"fleet/{fleet_id}")


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

@mcp.tool(description="List all transactions")
async def list_all_transactions():
    """List all transactions"""
    async with MarloMCPClient() as client:
        return await client.get("/transactions")


@mcp.tool(description="get market rates")
async def get_market_rates():
    """
    Fetch Market rates.

    """
    async with MarloMCPClient() as client:
        return await client.get(f"market-rates")


@mcp.tool(description="get market rate details")
async def get_market_rate_details(api_identifier: str):
    """
    Fetch Market rate details.
    
    Parameters:
    - api_identifier: The identifier of the market rate (e.g., 'IDS9SQAME2W2VRO93ON6HOL9TOI04E7S')
    """
    async with MarloMCPClient() as client:
        return await client.get(f"market-rates/{api_identifier}")


@mcp.tool(description="get covenant")
async def get_covenant():
    """
    Fetch Covenant.

    """
    async with MarloMCPClient() as client:
        return await client.get(f"covenant")
    

@mcp.tool(description="get credit score")
async def get_credit_score():
    """
    Fetch Credit Score
    """
    async with MarloMCPClient() as client:
        return await client.get(f"credit-score")


@mcp.tool(description="get interest rates")
async def get_interest_rates():
    """
    Fetch Interest Rates
    """
    async with MarloMCPClient() as client:
        return await client.get(f"interest-rates")


@mcp.tool(description="list all sanctions case manager")
async def list_all_sanctions_case_manager(page: int, per_page: int, schema: Optional[str] = None):
    """List all sanctions case manager"""
    async with MarloMCPClient() as client:
        return await client.get(f"list-sanction-case-manager", params={"page": page, "per_page": per_page, "schema": schema})


@mcp.tool(description="get sanctions case manager details")
async def get_sanctions_case_manager_details(source_id: str):
    """Get sanctions case manager details"""
    async with MarloMCPClient() as client:
        return await client.get(f"sanction-case-manager", params={"source_id": source_id})


@mcp.tool(description="search sanctions")
async def search_sanctions(request: SearchInputData):
    """Search sanctions"""
    async with MarloMCPClient() as client:
        return await client.post(f"sanctions", data=request.model_dump())


@mcp.tool(description="search individual sanction")
async def search_individual_sanction(source_id: str):
    """Search individual sanction"""
    async with MarloMCPClient() as client:
        return await client.get(f"sanction/{source_id}")


@mcp.tool(description="list all bank accounts")
async def list_all_bank_accounts():
    """List all bank accounts"""
    async with MarloMCPClient() as client:
        return await client.get("bank-accounts")


@mcp.tool(description="list all bank transactions")
async def list_all_bank_transactions(
    bank_id: str,
    status: Optional[str] = None,
    date_range: Optional[str] = None,
    amount_min: Optional[float] = None,
    amount_max: Optional[float] = None,
    base_type: Optional[list[str]] = None,
    search: Optional[str] = None,
    currency_code: Optional[str] = None,
    page: int = 1,
    per_page: int = 10
):
    """List all bank transactions with optional filters and pagination
    
    Args:
        bank_id: Bank account ID (required). Use list_all_bank_accounts to get available bank IDs
        status: Filter by status (MATCHED, UNMATCHED)
        date_range: Date range in format yyyy-MM-dd,yyyy-MM-dd
        amount_min: Minimum amount filter
        amount_max: Maximum amount filter
        base_type: Filter by base_type (DEBIT, CREDIT). Multiple values allowed
        search: Search term to filter transactions by (searches in transaction, invoice, bill fields)
        currency_code: Filter by currency code (e.g., USD, EUR)
        page: Page number (default 1)
        per_page: Items per page (default 10, max 100)
    """
    async with MarloMCPClient() as client:
        params = {
            "page": page,
            "per_page": per_page,
            "bank_id": bank_id
        }
        
        if status:
            params["status"] = status
        if date_range:
            params["date_range"] = date_range
        if amount_min is not None:
            params["amount_min"] = amount_min
        if amount_max is not None:
            params["amount_max"] = amount_max
        if base_type:
            params["base_type"] = base_type
        if search:
            params["search"] = search
        if currency_code:
            params["currency_code"] = currency_code
            
        return await client.get("bank-transactions", params=params)


@mcp.tool(description="get profit and loss data")
async def get_profit_loss(
    period_length: str,
    periods_to_compare: str,
    start_month: str
):
    """Get profit and loss data with specified parameters
    
    Args:
        period_length: Length of each period (e.g., "1" for monthly)
        periods_to_compare: Number of periods to compare (e.g., "6" for 6 months)
        start_month: Starting month in format "MMM YYYY" (e.g., "Aug 2025")
    """
    async with MarloMCPClient() as client:
        payload = {
            "periodLength": period_length,
            "periodsToCompare": periods_to_compare,
            "startMonth": start_month
        }
        return await client.post("profit-loss", data=payload)


@mcp.tool(description="get balance sheet data")
async def get_balance_sheet(
    period_length: str,
    periods_to_compare: str,
    start_month: str
):
    """Get balance sheet data with specified parameters
    
    Args:
        period_length: Length of each period (e.g., "1" for monthly)
        periods_to_compare: Number of periods to compare (e.g., "6" for 6 months)
        start_month: Starting month in format "MMM YYYY" (e.g., "Aug 2025")
    """
    async with MarloMCPClient() as client:
        payload = {
            "periodLength": period_length,
            "periodsToCompare": periods_to_compare,
            "startMonth": start_month
        }
        return await client.post("balance-sheet", data=payload)


@mcp.tool(description="Get a global search vessel valuation list")
async def get_global_search_vessel_list():
    """Get a global search vessel valuation list"""
    async with MarloMCPClient() as client:
        return await client.get("/global-vessel-search-list")


@mcp.tool(description="Get vessel valuation")
async def get_vessel_valuation(data: VesselValuationRequestSchema):
    """Get vessel valuation using DCF method"""
    async with MarloMCPClient() as client:
        return await client.post("vessel-valuation", data=data.model_dump())


@mcp.tool(description="List approval transactions")
async def list_approval_transactions():
    """List approval transactions"""
    async with MarloMCPClient() as client:
        return await client.get("/approval-transactions")


@mcp.tool(description="Get a global account currency balance")
async def get_global_account_currency_balance():
    """Get a global account currency balance"""
    async with MarloMCPClient() as client:
        return await client.get("/balances/current")


@mcp.tool(description="List all global accounts")
async def list_all_global_accounts():
    """List all global accounts"""
    async with MarloMCPClient() as client:
        return await client.get("/list-global-accounts")


@mcp.tool(description="List all payouts")
async def list_all_payouts():
    """List all payouts"""
    async with MarloMCPClient() as client:
        return await client.get("/list-payouts")


@mcp.tool(description="Get payout details")
async def get_payout_details(payout_id: str):
    """Get payout details"""
    async with MarloMCPClient() as client:
        return await client.get(f"/payout/{payout_id}")


@mcp.tool(description="Get a valuation of company")
async def get_company_valuation():
    """Get a valuation of company"""
    async with MarloMCPClient() as client:
        return await client.get("/company-valuation")


@mcp.tool(description="Get operational cashflow data")
async def get_operational_cashflow(
    period_length: str,
    periods_to_compare: str,
    start_month: str
):
    """Get operational cashflow data with specified parameters
    
    Args:
        period_length: Length of each period (e.g., "1" for monthly)
        periods_to_compare: Number of periods to compare (e.g., "6" for 6 months)
        start_month: Starting month in format "MMM YYYY" (e.g., "Aug 2025")
    """
    async with MarloMCPClient() as client:
        payload = {
            "periodLength": period_length,
            "periodsToCompare": periods_to_compare,
            "startMonth": start_month
        }
        return await client.post("operational-cashflow", data=payload)


@mcp.tool(description="Get cashbalance streams data")
async def get_cashbalance_streams():
    """Get cashbalance streams data"""
    async with MarloMCPClient() as client:
        return await client.get("cashbalance-streams")

    
def main():
    mcp.run()


if __name__ == "__main__":
    main()
