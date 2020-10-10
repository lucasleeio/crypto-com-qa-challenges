from behave import given, when, then

from pages import Exchange, Trade


@given('I am on exchange page')
def step_on_exchange(context):
    page = Exchange(context.driver, context.base_url)
    page.open()
    page.find_element(*page._accept_cookies_locator).click()


@when('I click "CRO Markets" tab')
def step_click_cro_markets(context):
    page = Exchange(context.driver, context.base_url)
    tabs = page.find_element(*page._tabs_locator)
    tabs.find_element(*page._cro_tab_locator).click()


@when('I click "CRO/USDC" item')
def step_click_cro_usdc(context):
    page = Exchange(context.driver, context.base_url)
    tbody = page.find_element(*page._tbody_locator)
    cro = tbody.find_element(*page._cro_usdc_locator)
    context.driver.execute_script("arguments[0].click();", cro)


@then('I should be on CRO/USDC trade page')
def step_on_cro_usdc_trade(context):
    page = Trade(context.driver, context.base_url)
    page.wait_for_page_to_load()
    assert page.find_element(*page._cro_usdc_locator).is_displayed()
