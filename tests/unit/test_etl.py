import pytest

pytestmark = pytest.mark.unit

def test_amount(rows):
    for r in rows:
        assert r["amount"] == r["price"] * r["qty"]

# @pytest.mark.parametrize("price, qty, amount", [
#     (2, 3, 6),
#     (5, 2, 10),
# ])
# def test_amount_parametrize(price, qty, amount):
#     assert amount == price * qty

def test_no_null(rows):
    for r in rows:
        assert r["price"] is not None