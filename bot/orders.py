from client import get_client
from logging_config import setup_logger

from binance.exceptions import BinanceAPIException


logger = setup_logger()

client = get_client()


def place_market_order(symbol, side, quantity):

    try:

        logger.info(
            f"Placing MARKET order | {symbol} | {side} | Qty: {quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET order success: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e}")

        print(f"\nBinance API Error:")
        print(f"Error Code : {e.code}")
        print(f"Message    : {e.message}")

        raise

    except Exception as e:

        logger.error(f"Unexpected Error: {e}")

        raise


def place_limit_order(symbol, side, quantity, price):

    try:

        logger.info(
            f"Placing LIMIT order | {symbol} | {side} | Qty: {quantity} | Price: {price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"LIMIT order success: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e}")

        print(f"\nBinance API Error:")
        print(f"Error Code : {e.code}")
        print(f"Message    : {e.message}")

        raise

    except Exception as e:

        logger.error(f"Unexpected Error: {e}")

        raise