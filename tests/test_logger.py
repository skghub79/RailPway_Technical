from core.logger import LoggerManager


def test_logger_creation():

    logger = LoggerManager.get_logger("test")

    assert logger is not None


def test_logger_name():

    logger = LoggerManager.get_logger("core")

    assert logger.name == "core"