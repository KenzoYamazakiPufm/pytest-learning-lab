import pytest
from api_client import ApiClient

@pytest.fixture(scope="session")
def api():
    c = ApiClient("https://httpbin.org")
    c.login("ken")
    return c
    