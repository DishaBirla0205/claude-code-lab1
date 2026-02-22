# Pricing service tests

from app.services.pricing import calculate_final_price


def test_premium_customer_pricing():
    price = calculate_final_price(100, "premium")
    assert price > 0


def test_standard_customer_pricing():
    price = calculate_final_price(100, "standard")
    assert price > 0
