import pytest
import requests

pytestmark = pytest.mark.api

@pytest.fixture(scope="module")
def resp():
    return requests.get("https://httpbin.org/get", timeout=10)

def test_status(resp):
    assert resp.status_code == 200

# def test_stringInJason(resp):
#     assert "args" in resp.json()

def test_speed(resp):
    assert resp.elapsed.total_seconds() < 5

def test_rows_shared(rows):
    assert len(rows) == 2