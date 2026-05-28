import logging


def setup_logger():
    logger = logging.getLogger("trading_bot")

    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:

        file_handler = logging.FileHandler("logs.txt")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger