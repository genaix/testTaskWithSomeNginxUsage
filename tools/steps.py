"""Steps for test view."""
# todo: may be replaced for allure.step later

from traceback import format_exception_only, format_tb
from functools import wraps
from typing import Callable


def step(title: str) -> Callable:
    """Step for test view.

    :param title:
    :return:
    """
    if callable(title):
        return StepContext(title.__name__, {})(title)
    else:
        return StepContext(title, {})


def format_traceback(exc_traceback):
    return ''.join(format_tb(exc_traceback)) if exc_traceback else None


def format_exception(etype, value):
    return '\n'.join(format_exception_only(etype, value)) if etype or value else None


class StepContext:
    """Contex manager step."""
    def __init__(self, title, params):
        """Constructor."""
        self.title = title
        self.params = params

    def __enter__(self):
        """Enter the context manager."""
        print(f"[step] {self.title}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager."""
        f_exc = format_exception(exc_type, exc_val)
        f_tb = format_traceback(exc_tb)
        # print(f"[step end] {self.title}")
        if f_exc:
            print(f_exc)
        if f_tb:
            print(f_tb)

    def __call__(self, func: Callable) -> Callable:
        """Use for step function."""
        @wraps(func)
        def impl(*a, **kw):
            with StepContext(self.title, {}):
                return func(*a, **kw)

        return impl
