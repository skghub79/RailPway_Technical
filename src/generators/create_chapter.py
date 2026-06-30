"""
RailPway_Technical

Module:
    create_chapter.py

Purpose:
    Generate a standard editable Word chapter for the
    Railway Permanent Way Maintenance Handbook.

Author:
    RailPway_Technical

Version:
    0.1.0
"""

from pathlib import Path


class ChapterGenerator:

    def __init__(self):
        self.version = "0.1.0"

    def create(self):
        print("=" * 60)
        print("RailPway_Technical")
        print("Chapter Generator")
        print("Version :", self.version)
        print("=" * 60)
        print("Chapter generation module loaded successfully.")
        print("=" * 60)


def main():

    app = ChapterGenerator()
    app.create()


if __name__ == "__main__":
    main()