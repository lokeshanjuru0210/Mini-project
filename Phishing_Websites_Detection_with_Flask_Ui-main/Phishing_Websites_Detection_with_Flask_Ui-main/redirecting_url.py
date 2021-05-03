import selenium
from selenium import webdriver


def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-translate")
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-autocomplete-off-autofill")
    options.add_argument("--no-first-run")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


def add_start_string(user_url=""):
    start_string = "http://"
    start_string_1 = "https://"
    if start_string in user_url:
        user_url = user_url
    elif start_string_1 in user_url:
        user_url = user_url
    else:
        user_url = start_string_1 + user_url

    return user_url


def open_url(user_url=""):
    options = chrome_options()
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    user_url = add_start_string(user_url)
    driver.get(user_url)


def redirect_user_url(user_url=""):
    options = chrome_options()
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    user_url = add_start_string(user_url)
    driver.get(user_url)
