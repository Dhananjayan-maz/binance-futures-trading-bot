from binance.client import Client
from dotenv import load_dotenv
from logging_config import setup_logger
import os
import time


# Load .env variables
load_dotenv()

# Setup logger
logger = setup_logger()


def get_client():
    try:
        api_key = os.getenv("API_KEY")
        secret_key = os.getenv("SECRET_KEY")

        client = Client(api_key, secret_key)

        # Binance Futures Testnet URL
        client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Dynamic server time synchronization
        server_time = client.get_server_time()

        system_time = int(time.time() * 1000)

        client.timestamp_offset = server_time["serverTime"] - system_time

        logger.info("Binance client connected successfully")

        return client

    except Exception as e:
        logger.error(f"Connection failed: {e}")
        print(f"Connection failed: {e}")
        raise