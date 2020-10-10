from pypom import Page
from selenium.webdriver.common.by import By


class Trade(Page):
    _page_content_locator = (By.CLASS_NAME, 'page-content')
    _spinner_locator = (By.CLASS_NAME, 'e-spinner')

    _cro_usdc_locator = (By.XPATH, '//*[@class="pair-toggle" and contains(text() ,"CRO/USDC")]')

    @property
    def loaded(self):
        page_content = self.find_element(*self._page_content_locator)
        spinner = self.find_element(*self._spinner_locator)
        return page_content.is_displayed() and not spinner.is_displayed()
