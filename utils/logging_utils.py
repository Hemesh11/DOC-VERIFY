import logging
import sys

def setup_logger(name='document_validation', log_level='INFO'):
    """
    Configure and return a logger with console handler only
    
    Args:
        name (str): Logger name
        log_level (str): Logging level
    
    Returns:
        logging.Logger: Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    logger.handlers.clear()

    # Console Handler only
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, log_level.upper()))
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)

    logger.addHandler(console_handler)
    return logger

# Global logger instance
logger = setup_logger()

def log_error(message, exc_info=None):
    logger.error(message, exc_info=exc_info)

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)
