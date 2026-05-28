import click

from validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from orders import (
    place_market_order,
    place_limit_order
)

from logging_config import setup_logger


logger = setup_logger()


@click.command()
@click.argument("symbol")
@click.argument("side")
@click.argument("order_type")
@click.argument("quantity")
@click.argument("price", required=False)

def main(symbol, side, order_type, quantity, price):

    try:

        # Validate inputs
        symbol = validate_symbol(symbol)

        side = validate_side(side)

        order_type = validate_order_type(order_type)

        quantity = validate_quantity(quantity)

        price = validate_price(price, order_type)

        # Print request summary
        print("\n===== ORDER REQUEST SUMMARY =====")

        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if order_type == "LIMIT":
            print(f"Price       : {price}")

        print("=================================\n")

        # Execute order
        if order_type == "MARKET":

            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        # Print response
        print("===== ORDER RESPONSE =====")

        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")

        avg_price = response.get("avgPrice")

        if avg_price:
            print(f"Average Price : {avg_price}")

        print("===========================\n")

        print("Order placed successfully")

        logger.info("Order placed successfully")

    except Exception as e:

        logger.error(f"CLI Error: {e}")

        print(f"Error: {e}")


if __name__ == "__main__":
    main()