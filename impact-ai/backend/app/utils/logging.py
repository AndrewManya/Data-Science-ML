"""Logging utilities."""

import logging
import json
from pythonjsonlogger import jsonlogger

def setup_logging(app_name: str):
    """Setup JSON logging."""
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    
    logger = logging.getLogger(app_name)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)
    
    return logger
