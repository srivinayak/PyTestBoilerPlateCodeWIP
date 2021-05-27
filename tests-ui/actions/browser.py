from typing import List
import logging
from selenium.webdriver.remote.webdriver import WebDriver

import actions

logger = logging.getLogger(__name__)


class BrowserActions:

    def __init__(self, driver):
        self._driver: WebDriver = driver
        #added on Monday 24MAY2021
        #self._driver: WebDriver = actions.remote_capabilities.MyRemoteWebDriver().remote_windows_firefox_driver()
        ##self._driver: WebDriver = actions.remote_capabilities.MyRemoteWebDriver().remote_windows_chrome_driver()

    def get_current_url(self) -> str:
        current_url = self._driver.current_url
        logger.info("Current URL is %s" % current_url)
        return current_url

    def get_title(self) -> str:
        title = self._driver.title
        logger.info("Current title is %s" % title)
        return title

    def get_current_tab_name(self) -> str:
        window_handle = self._driver.current_window_handle
        logger.debug("Current window handle is: %s" % str(window_handle))
        return window_handle

    def get_page_source(self) -> str:
        return self._driver.page_source

    def get_number_of_tabs(self) -> int:
        num_tabs = len(self._driver.window_handles)
        logger.info("Number of tabs: %s" % str(num_tabs))
        return num_tabs

    def get_tab_list(self) -> List[str]:
        tab_list = self._driver.window_handles
        logger.debug("List of window handles %s" % str(tab_list))
        return tab_list

    def switch_to_tab_index(self, index: int):
        tab_name: str = self._driver.window_handles[index]
        logger.info("About to switch to tab: ", tab_name)
        self.switch_to_tab(tab_name)
        logger.info("Switched to new tab at index: %s successfully" % str(index))

    def switch_to_tab(self, tab_name: str):
        self._driver.switch_to.window(tab_name)
        logger.info("Switched to new tab: %s" % str(tab_name))

    def close_current_tab(self):
        self._driver.close()
        logger.info("Current tab closed")

    def close_tab_at_index(self, index: int):
        self.switch_to_tab_index(index)
        self._driver.close()
        logger.info("Closed the tab at index %s" % str(index))

    def close_tab(self, name: str):
        self.switch_to_tab(name)
        self._driver.close()
        logger.info("Closed the tab: %s" % str(name))

    def navigate_back(self):
        self._driver.back()
        logger.info("Navigated to previous page")

    def refresh(self):
        self._driver.refresh()
        logger.info("Page refresh successful")

    def resize_to(self, width, height):
        self._driver.set_window_size(width, height)
        logger.info("Window size set to width: %s, height: %s" % (width, height))

    def go_to_url(self, url: str):
        self._driver.get(url)
        logger.info("Navigated to URL: %s" % str(url))

    def go_to_protected_url(self, full_url: str, username: str, password: str):
        https = "https://"
        http = "http://"

        protocol = ""
        if full_url.startswith(https):
            protocol = https
        elif full_url.startswith(http):
            protocol = http

        url = full_url
        if protocol:
            url = full_url.replace(protocol, "")

        self._driver.get(f'{protocol}{username}:{password}@{url}')
