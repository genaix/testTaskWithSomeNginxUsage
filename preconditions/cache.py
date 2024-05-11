"""Cache preconditions."""
from dataclasses import dataclass
from typing import Tuple, List, Dict, Any

from pytest import fixture

from steps.cache import (
    get_index_page_until_cache_activation,
    stupid_wait_for_cache_drop,
)
from tools.thematic_clients.main_service import HttpClientMainService


@dataclass
class CacheConfig:
    CACHE_TIME: float
    CACHE_TIME_BIAS: float
    CALLS_TO_CACHE_ACTIVATE: int
    CALLS_TO_CACHE_REACTIVATE: int


@fixture(scope="session")
def cache_options() -> CacheConfig:
    """Get cache options."""
    # todo: take values from config
    return CacheConfig(
        CACHE_TIME=2.,
        CACHE_TIME_BIAS=1.,
        CALLS_TO_CACHE_ACTIVATE=2,
        CALLS_TO_CACHE_REACTIVATE=1
    )


@fixture
def prec_drop_cache_wait(
        prec_http_client_main_service: HttpClientMainService,
        cache_options: CacheConfig
) -> List[Tuple[Dict[str, Any], float]]:
    """Prepare dropped cache via wait time.

    :return: results (response, time wait) if uncached call
    """
    results = []
    response, time_wait = prec_http_client_main_service.index()
    if time_wait < 1.:
        stupid_wait_for_cache_drop(cache_options.CACHE_TIME + cache_options.CACHE_TIME_BIAS)
        return results

    results.append((response, time_wait))
    return results


@fixture
def prec_active_cache_wait(
        prec_http_client_main_service: HttpClientMainService,
        cache_options: CacheConfig
) -> List[Tuple[Dict[str, Any], float]]:
    """Prepare dropped cache via wait time.

    :return: (response, time wait)
    """
    results = get_index_page_until_cache_activation(
        prec_http_client_main_service,
        cache_options.CALLS_TO_CACHE_ACTIVATE + 1
    )
    return results
