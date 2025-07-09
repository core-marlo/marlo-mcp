import os
import httpx
from typing import Any, Dict, Optional


class MarloMCPError(Exception):
    pass

class MarloMCPClient:
    """
    A client for the Marlo MCP server.
    
    Args:
        base_url: The base URL of the Marlo MCP server.
        api_key: The API key for the Marlo MCP server.
    """
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        self.mcp_server_url = base_url or os.getenv("MARLO_MCP_URL") or "https://api-app.marlo.online/mcp"
        self.api_key = api_key or os.getenv("MARLO_MCP_API_KEY")
        self._client: Optional[httpx.AsyncClient] = None

        if not self.api_key:
            raise MarloMCPError("Marlo MCP API key is required. Set MARLO_MCP_API_KEY environment variable or pass it to the constructor.")
        
    async def __aenter__(self):
        """Initialize and return an HTTP session for making requests to the Marlo MCP server.
        
        This method is called when entering an async context manager. It sets up
        the necessary HTTP client session with authentication headers and any
        required configuration for communicating with the MCP server.
        
        Returns:
            MarloMCPClient: The configured client instance ready for making requests.
        """
        self._client = httpx.AsyncClient(
            base_url=self.mcp_server_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "X-SOURCE": "marlo-mcp",
            },
            timeout=30,
        )
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        """Clean up the HTTP client session when exiting the async context.
        
        This method is called when exiting an async context manager. It ensures
        that the HTTP client session is properly closed and resources are released.
        """
        if self._client:
            await self._client.aclose()
            self._client = None

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request to the specified endpoint with optional parameters.
        
        Args:
            endpoint (str): The path of the endpoint to request.
            params (Optional[Dict[str, Any]]): Optional query parameters to include in the request.
            
        Returns:
            dict: The JSON response from the server.
        """
        if not self._client:
            raise MarloMCPError("Client not initialized. Ensure you are using the client in an async context.")
        
        try:
            response = await self._client.get(f"/{endpoint.lstrip('/')}", params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise MarloMCPError(f"HTTP error occurred: {e}")
    
    async def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make a POST request to the specified endpoint with the given data.
        
        Args:
            endpoint (str): The path of the endpoint to request.
            data (Dict[str, Any]): The data to send in the request body.
            
        Returns:
            dict: The JSON response from the server.
        """
        if not self._client:
            raise MarloMCPError("Client not initialized. Ensure you are using the client in an async context.")
        try:
            response = await self._client.post(f"/{endpoint.lstrip('/')}", json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise MarloMCPError(f"HTTP error occurred: {e}")