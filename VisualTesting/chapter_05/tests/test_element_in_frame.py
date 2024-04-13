from selenium.webdriver.common.by import By

from VisualTesting.chapter_05.tests.conftest import validate_frame


def test_element_in_frame(driver, eyes):
    frame = driver.find_element(By.TAG_NAME, 'iframe')
    validate_frame(driver, eyes,frame, (By.ID, 'tinymce'))