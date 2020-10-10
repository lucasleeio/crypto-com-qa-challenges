from behave import fixture, use_fixture

from selenium.webdriver import Chrome


@fixture
def selenium_webdriver_chrome(context):
    context.driver = Chrome()
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(selenium_webdriver_chrome, context)
    context.base_url = context.config.userdata.get('base_url', 'http://localhost')
