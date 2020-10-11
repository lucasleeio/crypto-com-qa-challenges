from pypom import Page
from selenium.webdriver.common.by import By


class Trade(Page):
    _page_content_locator = (By.CLASS_NAME, 'page-content')
    _spinner_locator = (By.CLASS_NAME, 'e-spinner')

    _cro_usdc_locator = (By.XPATH, '//*[@class="pair-toggle" and contains(text() ,"CRO/USDC")]')

    _depth_table_locator = (By.CLASS_NAME, 'depth-table')
    _depth_table_tbody_locator = (By.CLASS_NAME, 'tbody')
    _depth_table_item_locator = (By.CLASS_NAME, 'symbol-item')
    _depth_table_price_locator = (By.CLASS_NAME, 'price')
    _depth_table_amount_locator = (By.CLASS_NAME, 'amount')
    _depth_table_sum_locator = (By.CLASS_NAME, 'sum')

    _trade_form_locator = (By.CLASS_NAME, 'trade-form')
    _trade_form_block_locator = (By.CLASS_NAME, 'trade-block')
    _trade_form_input_locator = (By.CLASS_NAME, 'e-input-number')

    @property
    def loaded(self):
        page_content = self.find_element(*self._page_content_locator)
        spinner = self.find_element(*self._spinner_locator)
        return page_content.is_displayed() and not spinner.is_displayed()

    @property
    def cro_usdc(self):
        return self.find_element(*self._cro_usdc_locator)

    def get_depth_table_row_info(self, row):
        table_row = self.find_element(*self._depth_table_locator) \
            .find_elements(*self._depth_table_tbody_locator)[0 if row < 0 else 1] \
            .find_elements(*self._depth_table_item_locator)[row if row < 0 else row-1]
        price = table_row.find_element(*self._depth_table_price_locator).text
        amount = table_row.find_element(*self._depth_table_amount_locator).text
        sum = table_row.find_element(*self._depth_table_sum_locator).text

        return table_row, price, amount, sum

    def get_trade_form_info(self, bs):
        if bs == 'buy':
            block = 0
        elif bs == 'sell':
            block = 1
        else:
            raise ValueError
        trade_block = self.find_element(*self._trade_form_locator) \
            .find_elements(*self._trade_form_block_locator)[block]
        price = trade_block.find_elements(*self._trade_form_input_locator)[0].get_attribute('value')
        amount = trade_block.find_elements(*self._trade_form_input_locator)[1].get_attribute('value')
        volume = 0

        return price, amount, volume
