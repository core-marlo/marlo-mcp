# Marlo MCP Client

A Python client for interacting with the Marlo MCP (Maritime Control Platform) server. This package provides an async client for making authenticated requests to the MCP API, and includes example tools for vessel data retrieval.

## Features
- Async HTTP client for Marlo MCP API
- Easy authentication via API key
- Example usage for vessel data retrieval

## Requirements
- Python 3.12+
- [httpx](https://www.python-httpx.org/) (installed automatically)
- [mcp[cli]](https://pypi.org/project/mcp/) (installed automatically)

## Installation

Clone this repository and install dependencies:

```bash
pip install -e .
```

Or, if you just want to install dependencies:

```bash
pip install httpx>=0.28.1 mcp[cli]>=1.10.1
```

## 🔌 MCP Setup

here the example use for consume the mcp server

```json
{
    "mcpServers": {
        "marlo-mcp": {
            "command": "uv",
            "args": ["run", 
            "--with",
            "mcp[cli]",
            "mcp",
            "run",
            "PATH/TO/main.py"
            ],
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

## Usage

![Example usage of Marlo MCP Client](marlo_claude_example.png)

## 🔑 License
[MIT](LICENSE)
