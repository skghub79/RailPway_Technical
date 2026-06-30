"""
===============================================================================
RailPway_Technical
-------------------------------------------------------------------------------
Module      : constants.py
Purpose     : Global application constants
Author      : Sirshendu Karmakar
Version     : 0.1.0
Python      : 3.12+
===============================================================================
"""

from pathlib import Path


class AppInfo:
    """Application information."""

    NAME: str = "RailPway_Technical"
    TITLE: str = "Basic Technical Reference for Railway Permanent Way Maintenance"
    VERSION: str = "0.1.0"
    AUTHOR: str = "Sirshendu Karmakar"
    COMPANY: str = "Indian Oil Corporation Limited"
    COPYRIGHT: str = "© 2026"


class FolderName:
    """Standard project folders."""

    HANDBOOK = "handbook"
    CONFIG = "config"
    TEXT = "text"
    IMAGES = "images"
    DIAGRAMS = "diagrams"
    REFERENCES = "references"
    OUTPUT = "output"
    TEMPLATES = "templates"

    IMAGE_LIBRARY = "image_library"

    DOCS = "docs"

    TESTS = "tests"

    LOGS = "logs"

    DATABASE = "database"


class FileName:
    """Master configuration files."""

    SETTINGS = "settings.yaml"

    HANDBOOK_CONFIG = "handbook_config.xlsx"

    CHAPTER_INDEX = "chapter_index.xlsx"

    IMAGE_MANIFEST = "image_manifest.xlsx"

    TABLE_MANIFEST = "table_manifest.xlsx"

    GLOSSARY = "glossary.xlsx"

    REFERENCES = "references.xlsx"

    REVISION_HISTORY = "revision_history.xlsx"


class Extension:
    """Supported file extensions."""

    WORD = ".docx"

    PDF = ".pdf"

    HTML = ".html"

    EPUB = ".epub"

    IMAGE = ".jpg"

    SVG = ".svg"

    PNG = ".png"

    XLSX = ".xlsx"

    YAML = ".yaml"

    SQLITE = ".db"


class Naming:
    """Naming conventions."""

    CHAPTER = "V{volume:02d}_CH{chapter:03d}_{name}"

    FIGURE = "V{volume:02d}_CH{chapter:03d}_FIG{figure:03d}_{name}"

    TABLE = "V{volume:02d}_CH{chapter:03d}_TAB{table:03d}_{name}"

    DIAGRAM = "V{volume:02d}_CH{chapter:03d}_DIA{diagram:03d}_{name}"


class WordStyle:
    """Default Word formatting."""

    FONT_NAME = "Calibri"

    FONT_SIZE = 11

    TITLE_SIZE = 24

    HEADING1 = 16

    HEADING2 = 14

    HEADING3 = 12

    CAPTION = 10


class ImageSetting:
    """Image defaults."""

    MAX_WIDTH_CM = 15

    DEFAULT_DPI = 300


class Database:
    """Database configuration."""

    FILE_NAME = "RailPway_Technical.db"

    VERSION = 1


class LogSetting:
    """Logging configuration."""

    LOG_FOLDER = "logs"

    LOG_FILE = "RailPway_Technical.log"

    LEVEL = "INFO"

    FORMAT = (
        "%(asctime)s | "
        "%(levelname)-8s | "
        "%(name)s | "
        "%(message)s"
    )


class ExitCode:
    """Application exit codes."""

    SUCCESS = 0

    WARNING = 1

    ERROR = 2


class ProjectPath:
    """
    Helper methods for commonly used paths.
    """

    @staticmethod
    def root() -> Path:
        return Path.cwd()

    @staticmethod
    def handbook() -> Path:
        return ProjectPath.root() / FolderName.HANDBOOK

    @staticmethod
    def config() -> Path:
        return ProjectPath.handbook() / FolderName.CONFIG

    @staticmethod
    def output() -> Path:
        return ProjectPath.root() / FolderName.OUTPUT

    @staticmethod
    def logs() -> Path:
        return ProjectPath.root() / FolderName.LOGS