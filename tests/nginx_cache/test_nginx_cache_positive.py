"""Positive tests for nginx_cache."""

from pytest import mark
from pytest_check import check_functions

from steps.cache import get_index_page_until_cache_activation, make_calls_index_for_times_count
from tools.steps import step

pytestmark = [mark.nginx_cache]


def test_cache_activate(cache_options, prec_http_client_main_service, prec_drop_cache_wait):
    """Check cache activation.

    prec: start with dropped cache
    1. Make some calls of index
    2. Check for present cached results
    3. Check for present uncached results before cached
    """
    results = []
    results_drop = prec_drop_cache_wait
    results.extend(results_drop)

    with step("Make some calls of index"):
        results_active = get_index_page_until_cache_activation(
            prec_http_client_main_service,
            cache_options.CALLS_TO_CACHE_ACTIVATE + 1
        )

    with step("Check for present cached results"):
        check_functions.less(
            len(results_active),
            cache_options.CALLS_TO_CACHE_ACTIVATE + 1,
            "All tries get cached result exhausted"
        )
        results.extend(results_active)

    with step("Check for present uncached results before cached"):
        check_functions.greater(results[0][1], 1., "Uncached results should present before cached")

    # todo: if we provide for this test runs first after nginx startup -
    # then add check for equal uncached results to cache_options.CALLS_TO_CACHE_ACTIVATE


def test_cache_reactivate(cache_options, prec_http_client_main_service, prec_drop_cache_wait):
    """Check cache reactivation.

    prec: start with dropped cache
    1. Make call check have uncached results
    2. Make call check should have cached result
    """
    results = []
    results_drop = prec_drop_cache_wait
    results.extend(results_drop)

    with step("Make call check have uncached results"):
        # I would ask about requirements CALLS_TO_CACHE_REACTIVATE if our product under testing
        results_reactivate = make_calls_index_for_times_count(
            prec_http_client_main_service,
            cache_options.CALLS_TO_CACHE_REACTIVATE - len(results)
        )
        results.extend(results_reactivate)

        for i in range(len(results)):
            check_functions.greater(results[i][1], 1., "Uncached results number %i should present before cached" % i)

    with step("Make call check should have cached result"):
        response, time_wait = prec_http_client_main_service.index()
        check_functions.less(
            time_wait,
            1.,
            "Cached results should present after %i uncached calls" % cache_options.CALLS_TO_CACHE_REACTIVATE
        )
