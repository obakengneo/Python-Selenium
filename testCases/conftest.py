from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='C:\WebDriver\chromedriver.exe')  # make sure this path is right
    elif browser == 'edge':
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


##################### PyTest HTML Reports #####################

def pytest_configure(config):
    config._metadata['Project Name'] = 'RiseApp'
    config._metadata['Module Name'] = 'Nationalities'
    config._metadata['Tester'] = 'Obakeng'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
