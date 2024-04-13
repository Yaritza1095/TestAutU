from VisualTesting.chapter_05.tests.conftest import validate_window


def test_full_page_screenshots(driver, eyes):
    validate_window(driver, eyes)