"""
RailPway_Technical

Module:
    sqlite_manager.py

Purpose:
    SQLite database manager.

Author:
    Sirshendu Karmakar

Version:
    0.1.0
"""

import sqlite3
from pathlib import Path

from core.logger import logger


class SQLiteManager:
    """
    SQLite Database Manager
    """

    def __init__(self, db_file: Path):

        self.db_file = db_file

        self.connection = None

        self.cursor = None

    # ---------------------------------------------------------

    def connect(self):

        logger.info("Connecting SQLite database...")

        self.connection = sqlite3.connect(self.db_file)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        logger.info("Connected.")

    # ---------------------------------------------------------

    def close(self):

        if self.connection:

            self.connection.close()

            logger.info("Database closed.")

    # ---------------------------------------------------------

    def execute(self, sql: str, values=None):

        if values is None:

            self.cursor.execute(sql)

        else:

            self.cursor.execute(sql, values)

    # ---------------------------------------------------------

    def executemany(self, sql: str, values):

        self.cursor.executemany(sql, values)

    # ---------------------------------------------------------

    def commit(self):

        self.connection.commit()

    # ---------------------------------------------------------

    def fetchall(self):

        return self.cursor.fetchall()

    # ---------------------------------------------------------

    def fetchone(self):

        return self.cursor.fetchone()

    # ---------------------------------------------------------

    def create_tables(self):

        logger.info("Creating master tables...")

        self.execute("""
        CREATE TABLE IF NOT EXISTS chapters(
            id INTEGER PRIMARY KEY,
            volume TEXT,
            chapter_no INTEGER,
            chapter_code TEXT,
            chapter_name TEXT,
            pages INTEGER,
            figures INTEGER,
            status TEXT
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS figures(
            id INTEGER PRIMARY KEY,
            image_name TEXT,
            caption TEXT,
            chapter_code TEXT,
            image_type TEXT,
            license TEXT
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS glossary(
            id INTEGER PRIMARY KEY,
            term TEXT,
            abbreviation TEXT,
            definition TEXT
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS references(
            id INTEGER PRIMARY KEY,
            ref_id TEXT,
            document TEXT,
            edition TEXT,
            publisher TEXT
        )
        """)

        self.commit()

        logger.info("Database initialized successfully.")