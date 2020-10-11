from behave import when, then

import requests
import logging
from datetime import datetime, timedelta
import allure
from allure_commons.types import AttachmentType


@when('I send a request using the API')
def step_send_request(context):
    context.response = requests.get(context.config.userdata.get('api_endpoint', ''))


@then('the API should response success')
def step_response_success(context):
    logging.info(f'Status code: {context.response.status_code}')
    allure.attach(f'{context.response.status_code}', name='Status code', attachment_type=AttachmentType.TEXT)
    assert context.response.ok


@then('I extract the relative humidity for the day after tomorrow')
def step_extract_humidity(context):
    today_date = datetime.now().date()
    target_date = today_date + timedelta(days=2)
    target_date_str = datetime.strftime(target_date, '%Y%m%d')

    forecast_detail = context.response.json()['forecast_detail']
    target_forecast = list(filter(lambda x: x['forecast_date'] == target_date_str, forecast_detail))[0]

    target_humidity = f"{target_forecast['min_rh']} - {target_forecast['max_rh']}%"

    logging.info(f'Relative humidity: {target_humidity}')
    allure.attach(f'{target_humidity}', name='Relative humidity', attachment_type=AttachmentType.TEXT)
