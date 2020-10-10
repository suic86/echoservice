import json
import logging
import time

import pytest

from echoservice import create_app, db, Payload


@pytest.fixture
def app():
    _app = create_app()
    _app.logger.setLevel(logging.CRITICAL)
    ctx = _app.test_request_context()
    ctx.push()

    _app.config["TESTING"] = True
    _app.testing = True

    # In-memory sqlite db
    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    with _app.app_context():
        db.create_all()

    yield _app
    ctx.pop()


@pytest.fixture
def client(app):
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


def test_save_payload(echo_request):
    response, payload = echo_request
    assert json.loads(Payload.query.first().payload) == payload
