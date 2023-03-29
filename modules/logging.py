import logging
import sys

def initialize_logger():
    """ Initialize the global logger for this utility."""
    global logger
    logger = logging.getLogger()

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    handler.addFilter(lambda record: record.levelno <= logging.INFO)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    error_handler.setLevel(logging.WARNING)
    logger.addHandler(error_handler)
    return logger
