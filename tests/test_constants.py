from core.constants import AppInfo
from core.constants import Extension


def test_app_name():

    assert AppInfo.NAME == "RailPway_Technical"


def test_word_extension():

    assert Extension.WORD == ".docx"