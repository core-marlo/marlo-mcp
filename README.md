A Python client for interacting with the Marlo MCP (Model Context Protocol) server. This package provides an async client for making authenticated requests to the MCP API and includes example tools for vessel data retrieval.

## What is Marlo?
Marlo is a finance and operations platform designed for maritime and shipping companies.

Marlo helps shipping businesses manage their entire operations from a single platform. It offers tools for:
- Voyage Management: Plan routes, track progress, and log updates for each voyage.
- Banking: Manage accounts in multiple currencies, send and receive payments, and access maritime-focused banking features like global accounts and borderless cards.
- Loans & Finance: Request and track loans for cargo contracts, demurrage, and other financing needs. It also helps monitor covenants and keep financial records in order.
- Analytics: View up-to-date financial and operational data in one dashboard, including cashflow, valuations, and credit scores.
- Accounting: Sync with accounting software to maintain accurate financial records.
- Email Integration: Centralize all chartering and operations emails with filters and tags for easy sorting.
- Risk & Compliance: Track compliance, screen counterparties against global sanctions lists, monitor loan terms, and manage carbon intensity and emissions reporting.

Marlo is designed for various roles in the maritime industry, including CEOs, CFOs, chartering managers, operations managers, accountants, vessel owners, operators, and commercial managers. Its goal is to simplify operations, ensure compliance, and help maritime businesses grow.
To subscribe to Marlo or request a demo, simply email our team at [support@marlo.online](mailto:support@marlo.online). We're happy to help you get started!

## Features
- Async HTTP client for Marlo MCP API
- Easy authentication via API key
- Example usage for vessel data retrieval

## Requirements
- Python 3.12+
- uvx [guide](https://docs.astral.sh/uv/getting-started/installation/)
- [httpx](https://www.python-httpx.org/) (installed automatically)
- [mcp[cli]](https://pypi.org/project/mcp/) (installed automatically)

## 🔌 MCP Setup

here the example use for consume the mcp server

```json
{
    "mcpServers": {
        "marlo-mcp": {
            "command": "uvx",
            "args": ["marlo-mcp"],
            "env": {
                "MARLO_MCP_API_KEY": "<your-api-key>"
            }
        }
    }
}
```

For Claude Desktop, you can install and interact with it right away by running:

```bash
mcp install PATH/TO/main.py -v MARLO_MCP_API_KEY=<your-api-key>
```
## Available tools
The Marlo MCP client provides the following tools:

- `get_vessels`: Get all available vessels with minimal vessel details
- `get_vessel_details`: Get details of a specific vessel
- `create_vessel`: Create a new vessel
- `search_ports`: Search multiple ports
- `search_cargos`: Search for cargos
- `get_all_charter_specialists`: Get all available charter specialists
- `search_charterer_contacts`: Search for charterer contacts
- `get_all_voyages`: Get all voyages
- `get_voyage_details`: Get details of a specific voyage
- `get_voyage_profit_and_loss`: Get voyage profit and loss
- `get_all_estimates_sheet`: Get all estimates sheet
- `get_estimate_sheet_details`: Get details of a specific estimate sheet
- `get_all_cargo_books`: Get all cargo books
- `get_cargo_book_details`: Get details of a specific cargo book
- `list_all_vessel_fixtures`: List all vessel fixtures
- `get_vessel_fixture_details`: Get details of a specific vessel fixture
- `get_voyage_contacts`: Get voyage contacts
- `get_voyage_contacts_financial_details`: Get financial details for voyage contacts
- `get_vessel_fixture_contacts`: Get contacts for a vessel fixture
- `get_vessel_fixture_contacts_financial_details`: Get financial details for vessel fixture contacts
- `get_invoice_details`: Get invoice details
- `get_bill_details`: Get bill details
- `voyage_port_disbursements`: Get voyage port disbursements
- `get_voyage_laytime`: Get voyage laytime
- `list_all_customers`: List all customers
- `list_all_vendors`: List all vendors
- `list_all_lendors`: List all lendors
- `get_customer_details`: Get customer details
- `get_vendor_details`: Get vendor details
- `list_all_bills`: List all bills
- `list_all_invoices`: List all invoices
- `get_journal_entries`: Get journal entries
- `list_all_vendor_credits`: List all vendor credits
- `get_vendor_credit_details`: Get vendor credit details
- `list_all_credit_notes`: List all credit notes
- `get_credit_note_details`: Get credit note details
- `list_all_external_loans`: List all external loans
- `get_external_loan_details`: Get external loan details
- `list_all_marlo_loans`: List all marlo loans

## Usage

![Example usage of Marlo MCP Client](https://raw.githubusercontent.com/core-marlo/marlo-mcp/main/marlo_mcp/marlo_claude_example.png)

## 🔑 License
[MIT](LICENSE) © 2025 Marlo

