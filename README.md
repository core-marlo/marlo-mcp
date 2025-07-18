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

- `get_vessels`: Get all available vessels
- `get_vessel_details`: Get details of a specific vessel
- `create_vessel`: Create a new vessel in your fleet
- `create_estimate_sheet`: Create a new estimate sheet
- `calculate_voyage_estimate`: Calculate voyage estimate
- `search_ports`: Search for ports
- `search_cargos`: Search for cargos
- `search_charterer_contacts`: Search for charterer contacts
- `get_all_charter_specialists`: Get all available charter specialists

## Usage

![Example usage of Marlo MCP Client](https://raw.githubusercontent.com/core-marlo/marlo-mcp/main/marlo_mcp/marlo_claude_example.png)

## 🔑 License
[MIT](LICENSE) © 2025 Marlo

