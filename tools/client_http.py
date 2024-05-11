"""Http client basic."""

import httpx


class ClientHttp:
    def __init__(self, endpoint: str, follow_redirects: bool = True):
        """Initialize http client.

        :param endpoint: scheme://host:port
        :param follow_redirects: allow redirects
        """
        self.endpoint = endpoint
        self.follow_redirects = follow_redirects

    def request(self, method: str, url_path: str, params: dict = None, params_type: str = None) -> httpx.Response:
        """Request http unary wrapper.

        :param method: http method
        :param url_path: /index
        :param params: query
        :param params_type: json, query, file
        """
        url = f"{self.endpoint}{url_path}"
        # todo: extend functionality

        if method.upper() == "GET":
            return httpx.get(url, params=params, follow_redirects=self.follow_redirects)
        else:
            raise TypeError(f"HTTP method {method} is not supported by client.")
