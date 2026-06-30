"""
===============================================================================
RailPway_Technical
-------------------------------------------------------------------------------
Module      : logger.py
Purpose     : Central logging manager
Author      : Sirshendu Karmakar
Version     : 0.1.0
Python      : 3.12+
===============================================================================
"""

from __future__ import annotations

import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


class LoggerManager:
    """
    Central logging manager for the application.
    """

    _configured = False

    @classmethod
    def _configure(cls) -> None:
        if cls._configured:
            return

        log_folder = Path("logs")
        log_folder.mkdir(exist_ok=True)

        log_file = log_folder / "application.log"

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        if not root_logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            file_handler = TimedRotatingFileHandler(
                filename=log_file,
                when="midnight",
                interval=1,
                backupCount=30,
                encoding="utf-8",
            )
            file_handler.setFormatter(formatter)

            root_logger.addHandler(console_handler)
            root_logger.addHandler(file_handler)

        cls._configured = True

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Returns a configured logger instance.
        """
        cls._configure()
        return logging.getLogger(name)