# Pricing service module

from app.services.discounts import get_discount
from app.config.settings import SETTINGS


def calculate_final_price(base_price, customer_type):
    """
    Calculate the final price after applying discounts.
    """
    discount_rate = get_discount(customer_type)

    discounted_price = base_price * (1 - discount_rate)

    if SETTINGS.get("apply_tax"):
        tax_rate = SETTINGS.get("tax_rate", 0)
        discounted_price += discounted_price * tax_rate

    return round(discounted_price, 2)
