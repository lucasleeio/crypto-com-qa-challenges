from pypom import Page
from selenium.webdriver.common.by import By


class Exchange(Page):
    URL_TEMPLATE = '/exchange'

    _page_content_locator = (By.CLASS_NAME, 'page-content')
    _spinner_locator = (By.CLASS_NAME, 'e-spinner')

    _accept_cookies_locator = (By.CLASS_NAME, 'accept-cookies-button')

    _tabs_locator = (By.CLASS_NAME, 'e-tabs')
    _cro_tab_locator = (By.XPATH, '//*[text()="CRO Markets"]')

    _tbody_locator = (By.CLASS_NAME, 'home-tbody')
    _cro_usdc_locator = (By.XPATH, '//*[*[text()="CRO"] and *[text()="/USDC"]]')

    @property
    def loaded(self):
        page_content = self.find_element(*self._page_content_locator)
        spinner = self.find_element(*self._spinner_locator)
        return page_content.is_displayed() and not spinner.is_displayed()

    @property
    def accept_cookies(self):
        return self.find_element(*self._accept_cookies_locator)

    @property
    def cro_markets(self):
        return self.find_element(*self._tabs_locator) \
            .find_element(*self._cro_tab_locator)

    @property
    def cro_usdc(self):
        return self.find_element(*self._tbody_locator) \
            .find_element(*self._cro_usdc_locator)
