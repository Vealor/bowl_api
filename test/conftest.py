import pytest  # noqa: F401
from sanic import Sanic

Sanic.test_mode = True


def pytest_addoption(parser):
    parser.addoption("--nodb", action="store_true", help="disable db wiping")
