"""Cache preconditions."""
from dataclasses import dataclass
from time import sleep
from typing import Tuple, List, Dict, Any

from pytest import fixture

from tools.thematic_clients.main_service import HttpClientMainService


@dataclass
class CacheConfig:
    CACHE_TIME: float
    CALLS_TO_CACHE_ACTIVATE: int


@fixture(scope="session")
def cache_options() -> CacheConfig:
    """Get cache options."""
    # todo: take values from config
    return CacheConfig(CACHE_TIME=3., CALLS_TO_CACHE_ACTIVATE=2)


@fixture
def prec_drop_cache_wait(
        prec_http_client_main_service: HttpClientMainService,
        cache_options: CacheConfig
) -> Tuple[List[Tuple[Dict[str, Any], float]], bool]:
    """Prepare dropped cache via wait time.

    :return: ((response, time wait), wait status done)
    """
    results = []
    response, time_wait = prec_http_client_main_service.index()
    if time_wait < 1.:
        sleep(cache_options.CACHE_TIME)
        return results, True

    results.append((response, time_wait))
    return results, False
