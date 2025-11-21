"""
Logging utilities for the project.
"""

import logging
import sys
from pathlib import Path
from typing import Optional

from src.utils.constants import LOGS_PATH, LogConfig


def get_logger(
    name: str,
    level: Optional[str] = None,
    log_file: Optional[str] = None,
    console: bool = True,
) -> logging.Logger:
    """
    Get a configured logger instance.

    Args:
        name: Logger name (typically __name__ of calling module)
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file name (stored in logs/ directory)
        console: Whether to also log to console

    Returns:
        Configured logger instance

    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("Processing started")
    """
    # Create logger
    logger = logging.getLogger(name)

    # Set level
    log_level = level or LogConfig.LOG_LEVEL
    logger.setLevel(getattr(logging, log_level.upper()))

    # Clear existing handlers to avoid duplicates
    logger.handlers.clear()

    # Create formatter
    formatter = logging.Formatter(
        fmt=LogConfig.LOG_FORMAT, datefmt=LogConfig.LOG_DATE_FORMAT
    )

    # Add console handler if requested
    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # Add file handler if log_file specified
    if log_file:
        # Ensure logs directory exists
        LOGS_PATH.mkdir(parents=True, exist_ok=True)

        file_path = LOGS_PATH / log_file
        file_handler = logging.FileHandler(file_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger


def setup_logging(
    level: str = "INFO",
    log_file: Optional[str] = None,
    console: bool = True,
) -> None:
    """
    Setup logging configuration for the entire application.

    Args:
        level: Logging level
        log_file: Optional log file
        console: Whether to log to console

    Example:
        >>> setup_logging(level="DEBUG", log_file="app.log")
    """
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, level.upper()))

    # Clear existing handlers
    root_logger.handlers.clear()

    # Create formatter
    formatter = logging.Formatter(
        fmt=LogConfig.LOG_FORMAT, datefmt=LogConfig.LOG_DATE_FORMAT
    )

    # Console handler
    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

    # File handler
    if log_file:
        LOGS_PATH.mkdir(parents=True, exist_ok=True)
        file_path = LOGS_PATH / log_file
        file_handler = logging.FileHandler(file_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)


class LoggerMixin:
    """
    Mixin class to add logging capabilities to any class.

    Usage:
        class MyClass(LoggerMixin):
            def process(self):
                self.logger.info("Processing...")
    """

    @property
    def logger(self) -> logging.Logger:
        """Get logger for this class."""
        if not hasattr(self, "_logger"):
            self._logger = get_logger(
                f"{self.__class__.__module__}.{self.__class__.__name__}",
                log_file=LogConfig.LOG_FILE,
            )
        return self._logger


# Convenience function for quick logging
def log_info(message: str, logger_name: str = "app") -> None:
    """Quick info log."""
    logger = get_logger(logger_name)
    logger.info(message)


def log_warning(message: str, logger_name: str = "app") -> None:
    """Quick warning log."""
    logger = get_logger(logger_name)
    logger.warning(message)


def log_error(message: str, logger_name: str = "app", exc_info: bool = False) -> None:
    """Quick error log."""
    logger = get_logger(logger_name)
    logger.error(message, exc_info=exc_info)


def log_debug(message: str, logger_name: str = "app") -> None:
    """Quick debug log."""
    logger = get_logger(logger_name)
    logger.debug(message)
