from unittest.mock import Mock

import pytest
from selenium import webdriver

from praktikum.colors import Color
from data import Urls, MockEngine, MockFrame


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(Urls.MESTO)

    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def mock_engine():
    engine = Mock()
    engine.get_name.return_value = "MockedEngine123"
    engine.get_weight.return_value = MockEngine.WEIGHT

    return engine


@pytest.fixture(scope='function')
def mock_frame():
    frame = Mock()
    frame.get_color.return_value = Color.RED
    frame.get_weight.return_value = MockFrame.WEIGHT

    return frame

