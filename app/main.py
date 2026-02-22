# Main application entry point

from app.services.pricing import calculate_final_price
from app.utils.logger import log_info


def main():
    base_price = 100
    customer_type = "premium"

    final_price = calculate_final_price(base_price, customer_type)

    log_info(f"Final price for {customer_type} customer: {final_price}")


if __name__ == "__main__":
    main()
