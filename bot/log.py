import logging


def setup() -> None:
    """Set up loggers"""

    format_string = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    log_format = logging.Formatter(format_string)

    handler = logging.StreamHandler()
    handler.setFormatter(log_format)

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
