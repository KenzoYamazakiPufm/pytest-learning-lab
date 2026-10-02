import pytest

pytestmark = pytest.mark.unit

@pytest.fixture
def base():
    return 10

@pytest.fixture
def double(base):
    return base * 2

def test_double(double):
    assert double == 20

@pytest.fixture(autouse=True)
def banner():
    print("\n--- 开始 ---")