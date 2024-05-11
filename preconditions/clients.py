"""Client fixtures."""

from pytest import fixture

from tools.client_http import ClientHttp
from tools.thematic_clients.main_service import HttpClientMainService


@fixture(scope="session")
def prec_http_client() -> ClientHttp:
    """Fixture http client."""
    return ClientHttp("http://localhost", follow_redirects=True)
    # todo: use config


@fixture(scope="session")
def prec_http_client_main_service(prec_http_client: ClientHttp):
    """Fixture http client for main service."""
    return HttpClientMainService(prec_http_client)
