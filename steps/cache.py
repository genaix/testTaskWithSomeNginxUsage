"""Cache steps."""

from time import sleep
from typing import Tuple, List, Dict, Any

from tools.thematic_clients.main_service import HttpClientMainService


def get_index_page_until_cache_activation(
        client: HttpClientMainService,
        max_retries: int
) -> List[Tuple[Dict[str, Any], float]]:
    """Call index until get cached result.

    :param client: main service http client
    :param max_retries: max retries for call
    """
    results = []

    for i in range(max_retries):
        response, time = client.index()
        results.append((response, time))
        if time < 1.:
            break

    return results


def get_index_page_until_cache_drop(
        client: HttpClientMainService,
        max_retries: int
) -> List[Tuple[Dict[str, Any], float]]:
    """Call index until get uncached result.

    :param client: main service http client
    :param max_retries: max retries for call
    """
    results = []

    for i in range(max_retries):
        response, time = client.index()
        results.append((response, time))
        if time > 1.:
            break

    return results


# @step("sleep cache drop")
def stupid_wait_for_cache_drop(wait_time: float):
    """Wait for cache drop by time.

    :param wait_time: time waiting
    """
    sleep(wait_time)


def make_calls_index_for_times_count(
        client: HttpClientMainService,
        calls_count: int
) -> List[Tuple[Dict[str, Any], float]]:
    """Make calls index for times count

    :param client: main service http client
    :param calls_count: number of calls
    :return: responses and times count
    """
    results = []
    for i in range(calls_count):
        response, time_wait = client.index()
        results.append((response, time_wait))

    return results
