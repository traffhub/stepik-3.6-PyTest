import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     options = webdriver.ChromeOptions()
#     options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#     chrome_driver_binary = "C:\chromedriver\chromedriver.exe"
#     browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="eng",
                     help="Choose browser language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        chrome_driver_binary = "C:\chromedriver\chromedriver.exe"
        browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        binary = FirefoxBinary("F:\\Program Files\\Mozilla Firefox\\firefox.exe")
        firefox_driver_binary = "C:\\geckodriver\\geckodriver.exe"
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(capabilities=cap, executable_path=firefox_driver_binary, firefox_binary=binary,firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()