import pytest
from selene import browser
from selene.support.conditions import be, have


@pytest.fixture
def set_window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 1024


def test_search(set_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_zero_search(set_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('[dsftretyertgfresyerye').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
