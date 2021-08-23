"""
Functional test for /src/endpoints/general.py
"""
import pytest
from test._helpers import get_req
from test import api, test_client


@pytest.mark.general
class TestGeneralGet:
    async def test_health_version_success(self, test_client):
        response = await get_req("/api", test_client)

        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "ok"
        assert "VERSION" in data.keys()


@pytest.mark.general
class TestFailuresGet:
    async def test_400(self, test_client):
        response = await get_req("/api/?test=400", test_client)

        assert response.status_code == 400
        data = response.json()
        assert data.get("status") == "error"

    async def test_401(self, test_client):
        response = await get_req("/api/?test=401", test_client)

        assert response.status_code == 401
        data = response.json()
        assert data.get("status") == "error"

    async def test_403(self, test_client):
        response = await get_req("/api/?test=403", test_client)

        assert response.status_code == 403
        data = response.json()
        assert data.get("status") == "error"

    async def test_404(self, test_client):
        response = await get_req("/api/?test=404", test_client)

        assert response.status_code == 404
        data = response.json()
        assert data.get("status") == "error"

    async def test_408(self, test_client):
        response = await get_req("/api/?test=408", test_client)

        assert response.status_code == 408
        data = response.json()
        assert data.get("status") == "error"

    async def test_413(self, test_client):
        response = await get_req("/api/?test=413", test_client)

        assert response.status_code == 413
        data = response.json()
        assert data.get("status") == "error"

    async def test_417(self, test_client):
        response = await get_req("/api/?test=417", test_client)

        assert response.status_code == 417
        data = response.json()
        assert data.get("status") == "error"

    async def test_500(self, test_client):
        response = await get_req("/api/?test=500", test_client)

        assert response.status_code == 500
        data = response.json()
        assert data.get("status") == "error"

    async def test_503(self, test_client):
        response = await get_req("/api/?test=503", test_client)

        assert response.status_code == 503
        data = response.json()
        assert data.get("status") == "error"

    async def test_other(self, test_client):
        response = await get_req("/api/?test=other", test_client)

        assert response.status_code == 500
        data = response.json()
        assert data.get("status") == "error"
