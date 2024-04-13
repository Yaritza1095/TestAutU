from assertpy import assert_that
from time import sleep
from VisualTesting.chapter_05.page_objects.search_page import SearchPage
from VisualTesting.chapter_05.tests.conftest import validate_window



def test_filter_book(eyes, driver):
    page = SearchPage(driver)
    page.filter_books('Agile')
    validate_window(driver, eyes, tag = 'filter_text')