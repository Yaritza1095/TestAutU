import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumexercises.pages.search_page import GoogleSearchPage

def test_search_panda():
    browser = Chrome()
    search_page = GoogleSearchPage(browser)

    search_page.load()
    search_page.search('panda')

    # Wait for the search results to load
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'g'))
    )

    # Check that the first search result contains the word 'panda'
    first_result_text = browser.find_element(By.CSS_SELECTOR, '.g').text.lower()
    assert 'panda' in first_result_text

    browser.quit()
