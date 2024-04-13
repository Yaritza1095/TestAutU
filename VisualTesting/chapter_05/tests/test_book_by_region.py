from selenium.webdriver.common.by import By

from VisualTesting.chapter_05.tests.conftest import validate_element


def test_book_by_region(driver, eyes):
    element = driver.find_element(By.ID, 'pid3')
    validate_element(driver, eyes, element)