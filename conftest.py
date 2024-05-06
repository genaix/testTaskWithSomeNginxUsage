"""Basic conftest PyTest."""

# pytest_plugins = [
#     'preconditions.folder_name'
# ]


def pytest_addoption(parser):
    """Run tests parameters."""
    parser.addoption(
        "--config",
        default=None,
        action="store",
        help="Path to config file"
    )
