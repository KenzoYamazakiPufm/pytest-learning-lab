import config
import pytest

pytestmark = pytest.mark.unit

def test_with_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "fake-key")
    assert config.get_token() == "fake-key"

def test_without_key(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    assert config.get_token() == ""

def test_restore_works():
    assert config.get_token() == ""