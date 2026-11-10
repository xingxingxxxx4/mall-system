from coupon import calculate_price

def test_coupon():
    assert calculate_price(100, 20) == 80