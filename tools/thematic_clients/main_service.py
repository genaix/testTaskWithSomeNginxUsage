"""Client for main-service."""
from typing import Dict, Any, Tuple

from tools.client_http import ClientHttp
from tools.helpers import http_request_timed


class HttpClientMainService:
    """Client for main-service."""
    def __init__(self, http_client: ClientHttp):
        """Initialize HttpClientMainService."""
        self.http_client = http_client

    @http_request_timed
    def index(self) -> Tuple[Dict[str, Any], int]:
        """Get main page data."""
        response = self.http_client.request("GET", "", {})
        return response.json(), response.status_code  # todo: handle error json dump
