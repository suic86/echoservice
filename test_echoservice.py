import json
import time

import pytest

from echoservice import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


@pytest.fixture
def echo_request(client):
    payload = {"firstName": "John", "lastName": "Doe"}
    response = client.post(
        "/humai/echoservice", data=json.dumps(payload), content_type="application/json"
    ).json
    return response, payload


def test_contains_fields(echo_request):
    response, _ = echo_request
    assert "timestamp" in response
    assert "payload" in response


def test_payload_is_unchanged(echo_request):
    response, payload = echo_request
    assert response["payload"] == payload


def test_timestamp(echo_request):
    response, _ = echo_request
    current_timestamp = int(time.time())
    assert response["timestamp"] <= current_timestamp
    assert current_timestamp - response["timestamp"] < 1
