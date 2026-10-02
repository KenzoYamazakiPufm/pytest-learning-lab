import pytest
from etl import output

@pytest.fixture
def rows():
    return output()