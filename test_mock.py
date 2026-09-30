import pytest
import requests

def test_client_sends_right_url(monkeypatch):
    capture = {}

    class FakeResp:
        status_code = 200
        def json(self):
            return {}

    def fake_get(self, url, **kwargs):
        capture['url'] = url
        return FakeResp()

    monkeypatch.setattr("requests.Session.get", fake_get)

    from api_client import ApiClient
    c = ApiClient("http://api.test")
    c.get("/users")

    assert capture['url'] == "http://api.test/users"


def test_client_raise_on_network_error(monkeypatch):
    def fake_get(self, url, **kwargs):
        raise requests.ConnectionError("断网了")

    monkeypatch.setattr("requests.Session.get", fake_get)

    from api_client import ApiClient
    c = ApiClient("http://api.test")

    with pytest.raises(requests.ConnectionError):
        c.get("/users")