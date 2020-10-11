from behave import given, when, then
from hamcrest import assert_that, equal_to

from pages import Exchange, Trade


@given('I am on exchange page')
def step_on_exchange(context):
    page = Exchange(context.driver, context.base_url).open()
    page.accept_cookies.click()


@when('I click "CRO Markets" tab')
def step_click_cro_markets(context):
    page = Exchange(context.driver, context.base_url)
    page.cro_markets.click()


@when('I click "CRO/USDC" item')
def step_click_cro_usdc(context):
    page = Exchange(context.driver, context.base_url)
    page.cro_usdc.click()


@then('I should be on CRO/USDC trade page')
def step_be_on_cro_usdc_trade(context):
    page = Trade(context.driver, context.base_url).wait_for_page_to_load()
    assert page.cro_usdc.is_displayed()


@given('I am on CRO/USDC trade page')
def step_on_cro_usdc_trade(context):
    Trade(context.driver, context.base_url).wait_for_page_to_load()


@when('I click row "{row:d}" in depth table')
def step_click_depth_table_row(context, row):
    page = Trade(context.driver, context.base_url)
    page.get_depth_table_row(row).click()
    context.price, _, context.sum = page.get_depth_table_row_info(row)


@then('I should see its price and sum put into "{bs}" trade form')
def step_check_price_in_form(context, bs):
    page = Trade(context.driver, context.base_url)
    price, amount, _ = page.get_trade_form_info(bs)
    assert_that(price, equal_to(context.price))
    assert_that(amount, equal_to(context.sum))


@when('I input "{price}" into price of "{bs}" trade form')
def step_input_price(context, price, bs):
    page = Trade(context.driver, context.base_url)
    page.trade_form_input_price(bs, price)


@when('I input "{amount}" into amount of "{bs}" trade form')
def step_input_amount(context, amount, bs):
    page = Trade(context.driver, context.base_url)
    page.trade_form_input_amount(bs, amount)


@then('I should see "{total}" calculated in "{bs}" trade form')
def step_check_volume_in_form(context, total, bs):
    page = Trade(context.driver, context.base_url)
    _, _, volume = page.get_trade_form_info(bs)
    assert_that(volume, equal_to(total))
