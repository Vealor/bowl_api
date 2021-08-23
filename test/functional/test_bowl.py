"""
Functional test for /src/endpoints/general.py
"""
import pytest
from test._helpers import post_req
from test import api, test_client


@pytest.mark.bowl
class TestBowlPost:
    async def test_bowl_perfect_300(self, test_client):
        payload = [
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10, 10, 10
        ]

        response = await post_req("/api/bowl", test_client, payload)

        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "ok"
        assert data.get("payload") == 300

    async def test_bowl_fail_0(self, test_client):
        payload = [
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0
        ]

        response = await post_req("/api/bowl", test_client, payload)

        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "ok"
        assert data.get("payload") == 0

    async def test_bowl_149(self, test_client):
        payload = [
            8, 2,
            5, 4,
            9, 0,
            10,
            10,
            5, 5,
            5, 3,
            6, 3,
            9, 1,
            9, 1, 10
        ]

        response = await post_req("/api/bowl", test_client, payload)

        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "ok"
        assert data.get("payload") == 149

    async def test_bowl_133(self, test_client):
        payload = [
            1, 4,
            4, 5,
            6, 4,
            5, 5,
            10,
            0, 1,
            7, 3,
            6, 4,
            10,
            2, 8, 6
        ]

        response = await post_req("/api/bowl", test_client, payload)

        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "ok"
        assert data.get("payload") == 133

    async def test_bowl_186(self, test_client):
        payload = [
            5, 5,
            4, 0,
            8, 1,
            10,
            0, 10,
            10,
            10,
            10,
            4, 6,
            10, 10, 5
        ]

        response = await post_req("/api/bowl", test_client, payload)

        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "ok"
        assert data.get("payload") == 186

    async def test_bowl_all_spare(self, test_client):
        payload = [
            5, 5,
            5, 5,
            5, 5,
            5, 5,
            5, 5,
            5, 5,
            5, 5,
            5, 5,
            5, 5,
            5, 5, 0
        ]

        response = await post_req("/api/bowl", test_client, payload)

        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "ok"
        assert data.get("payload") == 145
