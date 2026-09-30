import pytest

@pytest.fixture(params=["dev", "prod"])
def env(request):                # ← 必须加 request
    return request.param         # ← 取当前那组值

def test_env(env):
    assert env in ("dev", "prod")
