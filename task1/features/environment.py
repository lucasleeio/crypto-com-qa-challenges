from behave import fixture, use_fixture

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


@fixture
def selenium_webdriver_chrome(context):
    options = Options()
    options.add_argument("window-size=1920,1080")
    options.add_argument("--disable-smooth-scrolling")
    options.add_argument("--log-level=3")
    if context.config.userdata.getbool('is_headless', True):
        options.add_argument("--headless")
    context.driver = Chrome(chrome_options=options)
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(selenium_webdriver_chrome, context)
    context.base_url = context.config.userdata.get('base_url', 'http://localhost')
