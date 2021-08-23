import pytest
# from ._helpers import seed_db_data
from src import build_api  # , db


@pytest.fixture(scope="module")
def api(request):
    api = build_api()
    yield api


@pytest.fixture(scope="function")
def test_client(loop, api, sanic_client):
    return loop.run_until_complete(sanic_client(api))
