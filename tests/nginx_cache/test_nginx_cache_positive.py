"""Positive tests for nginx_cache."""

from pytest import mark
from pytest_check import check_functions

from steps.cache import get_index_page_until_cache_activation

pytestmark = [mark.nginx_cache]


def test_cache_activate(cache_options, prec_http_client_main_service, prec_drop_cache_wait):
    """Check cache activation.

    1. Make some calls of index
    2. Check for present cached results
    3. Check for present uncached results before cached
    """
    results = []
    results_drop, _ = prec_drop_cache_wait
    results.extend(results_drop)
    results.extend(
        get_index_page_until_cache_activation(
            prec_http_client_main_service,
            cache_options.CACHE_TIME,
            cache_options.CALLS_TO_CACHE_ACTIVATE * 10
        )
    )

    check_functions.greater(results[0][1], 1., "Uncached results should present before cached")


def test_cache_activate_attempts(cache_options, prec_http_client_main_service, prec_drop_cache_wait):
    """Check cache activation exactly after configured calls.

    1. Make configured number calls of index
    2. Check count uncached results
    3. Next call should be cached
    """
    results = []
    results_drop, _ = prec_drop_cache_wait
    results.extend(results_drop)

    for i in range(cache_options.CALLS_TO_CACHE_ACTIVATE - len(results)):
        response, time_wait = prec_http_client_main_service.index()
        results.append((response, time_wait))

    for i in range(len(results)):
        check_functions.greater(results[i][1], 1., "Uncached results number %i should present before cached" % i)

    response, time_wait = prec_http_client_main_service.index()
    check_functions.less(
        time_wait,
        1.,
        "Cached results should present after uncached after %i calls" % cache_options.CALLS_TO_CACHE_ACTIVATE
    )
