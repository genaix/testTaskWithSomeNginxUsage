"""Negative tests for nginx_cache."""
from functools import reduce

from pytest import mark
from pytest_check import check_functions

from steps.cache import get_index_page_until_cache_drop, stupid_wait_for_cache_drop
from tools.steps import step

pytestmark = [mark.nginx_cache]


def test_cache_deactivate_after_tries(cache_options, prec_http_client_main_service, prec_drop_cache_wait):
    """Check cache deactivate after n seconds while calls.

    prec: start with dropped cache
    1. Call for some times to cache deactivation
    2. Last call should have uncached results
    3. Check time uncached calls
    """
    _ = prec_drop_cache_wait
    _results_drop = get_index_page_until_cache_drop(
        prec_http_client_main_service, int(cache_options.CACHE_TIME * 100)
    )

    with step("Call for some times to cache deactivation"):
        results_drop = get_index_page_until_cache_drop(
            prec_http_client_main_service, int(cache_options.CACHE_TIME * 100)
        )

    with step("Last call should have uncached results"):
        check_functions.greater(results_drop[-1][1], 1., "Uncached result should present after cached")

    with step("Check time uncached calls"):
        total_time = reduce(lambda x, y: x + y, [x[1] for x in results_drop[:-1]], 0.)
        check_functions.between(
            total_time,
            cache_options.CACHE_TIME,
            cache_options.CACHE_TIME + cache_options.CACHE_TIME_BIAS,
            f"Uncached results time total should be close to {cache_options.CACHE_TIME}"
        )


def test_cache_deactivate_after_wait(cache_options, prec_http_client_main_service, prec_active_cache_wait):
    """Check cache deactivate after n seconds.

    prec: start with active cache
    1. Wait for cache deactivation
    2. Call should have uncached results
    """
    results = []
    _ = prec_active_cache_wait

    # I would ask about requirements CACHE_TIME_BIAS if our product under testing, now it looks high
    stupid_wait_for_cache_drop(cache_options.CACHE_TIME + cache_options.CACHE_TIME_BIAS)

    response, time_wait = prec_http_client_main_service.index()
    results.append((response, time_wait))
    check_functions.greater(time_wait, 1., "Uncached result should present after wait")
