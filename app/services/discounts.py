# Discounts service module


def get_discount(customer_type):
    """
    Return discount rate based on customer type.
    """
    if customer_type == "premium":
        return 0.2
    elif customer_type == "standard":
        return 0.1
    else:
        return 0.0
