"""Cache steps."""

from typing import Tuple, List, Dict, Any

from pytest_check import check_functions

from tools.thematic_clients.main_service import HttpClientMainService


def get_index_page_until_cache_activation(
        client: HttpClientMainService,
        cache_time: float = 3,
        max_retries: int = 15
) -> List[Tuple[Dict[str, Any], float]]:
    """Call index until get cached result."""
    results = []

    for i in range(max_retries):
        response, time = client.index()
        results.append((response, time))
        if time < 1.:
            break

    check_functions.less(len(results), max_retries, "All tries get cached result exceeded")
    return results
