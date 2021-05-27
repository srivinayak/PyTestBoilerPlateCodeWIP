from assertpy import assert_that
from pytest_bdd import given, parsers
from pytest_selenium_enhancer import CustomWait
from selenium.webdriver.common.by import By

from actions.browser import BrowserActions
from page_objects.selenium_generics import SeleniumGenerics
from utils.locators import Locators


@given(parsers.re("I am on the url '(?P<page_url>.*)'"))
@given(parsers.re("I am on the site '(?P<page_url>.*)'"))
@given(parsers.re("I am on the page '(?P<page_url>.*)'"))
def open_webpage(browser: BrowserActions, base_url, page_url):
    browser.go_to_url(f"{base_url}{page_url}")


@given(parsers.re("I am on external url '(?P<site_url>.*)'"))
@given(parsers.re("I am on external site '(?P<site_url>.*)'"))
def open_external_webpage(browser: BrowserActions, site_url):
    browser.go_to_url(site_url)


@given(parsers.re("The element '(?P<locator_path>.*)' is displayed"))
def element_displayed(selenium, locators: Locators, locator_path):
    CustomWait(selenium).wait_for_element_visible(value=locators.parse_and_get(locator_path))


@given(parsers.re("The element '(?P<locator_path>.*)' is not displayed"))
def element_not_displayed(selenium, locators: Locators, locator_path):
    CustomWait(selenium).wait_for_element_not_visible(value=locators.parse_and_get(locator_path))


@given(parsers.re("The element '(?P<locator_path>.*)' is enabled"))
def element_enabled(selenium, locators: Locators, locator_path):
    locator = locators.parse_and_get(locator_path)
    CustomWait(selenium).wait_for_element_visible(value=locator)
    assert_that(selenium.find_element(By.XPATH, locator).is_enabled()).is_true()


@given(parsers.re("The element '(?P<locator_path>.*)' is not enabled"))
def element_not_enabled(selenium, locators: Locators, locator_path):
    locator = locators.parse_and_get(locator_path)
    CustomWait(selenium).wait_for_element_visible(value=locator)
    assert_that(selenium.find_element(By.XPATH, locator).is_enabled()).is_false()


@given(parsers.re("The element '(?P<locator_path>.*)' is selected"))
def element_selected(selenium, locators: Locators, locator_path):
    locator = locators.parse_and_get(locator_path)
    CustomWait(selenium).wait_for_element_visible(value=locator)
    assert_that(selenium.find_element(By.XPATH, locator).is_selected()).is_true()


@given(parsers.re("The element '(?P<locator_path>.*)' is not selected"))
def element_not_selected(selenium, locators: Locators, locator_path):
    locator = locators.parse_and_get(locator_path)
    CustomWait(selenium).wait_for_element_visible(value=locator)
    assert_that(selenium.find_element(By.XPATH, locator).is_selected()).is_false()


@given(parsers.re("There is an element '(?P<locator_path>.*)' on the page"))
def element_exists(selenium, locators: Locators, locator_path):
    CustomWait(selenium).wait_for_element_visible(value=locators.parse_and_get(locator_path))


@given(parsers.re("There is no element '(?P<locator_path>.*)' on the page"))
def element_not_exists(selenium, locators: Locators, locator_path):
    CustomWait(selenium).wait_for_element_not_visible(value=locators.parse_and_get(locator_path))


@given(parsers.re("The title is '(?P<title>.*)'"))
def page_title(selenium, title):
    assert_that(selenium.title).is_equal_to(title)


@given(parsers.re("The title is not '(?P<title>.*)'"))
def page_title(selenium, title):
    assert_that(selenium.title).is_not_equal_to(title)


@given(parsers.re("The button '(?P<locator_path>.*)' text is '(?P<text>.*)'"))
@given(parsers.re("The element '(?P<locator_path>.*)' text is '(?P<text>.*)'"))
def element_equals_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).is_equal_to(text)


@given(parsers.re("The button '(?P<locator_path>.*)' text is not '(?P<text>.*)'"))
@given(parsers.re("The element '(?P<locator_path>.*)' text is not '(?P<text>.*)'"))
def element_not_equals_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).is_not_equal_to(text)


@given(parsers.re("The element '(?P<locator_path>.*)' contains the text '(?P<text>.*)'"))
@given(parsers.re("The button '(?P<locator_path>.*)' contains the text '(?P<text>.*)'"))
def contains_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).contains(text)


@given(parsers.re("The element '(?P<locator_path>.*)' does not contain the text '(?P<text>.*)'"))
@given(parsers.re("The button '(?P<locator_path>.*)' does not contain the text '(?P<text>.*)'"))
def does_not_contain_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).does_not_contain(text)


@given(parsers.re("The button '(?P<locator_path>.*)' does not contain any text"))
@given(parsers.re("The element '(?P<locator_path>.*)' does not contain any text"))
def does_not_contain_any_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).matches(r'^$')


@given(parsers.re("The button '(?P<locator_path>.*)' contains any text"))
@given(parsers.re("The element '(?P<locator_path>.*)' contains any text"))
def contains_any_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).matches(r'(.*?)')


@given(parsers.re("The page url is '(?P<url>.*)'"))
def given_page_url_is(selenium, url):
    assert_that(selenium.current_url).is_equal_to(url)


@given(parsers.re("The page url is not '(?P<url>.*)'"))
def given_page_url_is_not(selenium, url):
    assert_that(selenium.current_url).is_not_equal_to(url)


@given(parsers.re("The attribute '(?P<attribute>.*)' of element '(?P<locator_path>.*)' is the value '(?P<value>.*)'"))
def check_property_is(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, value, attribute):
    actual_value = selenium_generics.get_attribute_of_element(locators.parse_and_get(locator_path), attribute)
    assert_that(actual_value).is_equal_to(value)


@given(parsers.re("The attribute '(?P<attribute>.*)' of element '(?P<locator_path>.*)' is not the value '(?P<value>.*)'"))
def check_property_is_not(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, value, attribute):
    actual_value = selenium_generics.get_attribute_of_element(locators.parse_and_get(locator_path), attribute)
    assert_that(actual_value).is_not_equal_to(value)


@given(parsers.re("The css attribute '(?P<attribute>.*)' of element '(?P<locator_path>.*)' is the value '(?P<value>.*)'"))
def check_css_property_is(attribute, selenium_generics: SeleniumGenerics, locators: Locators, locator_path, value):
    actual_value = selenium_generics.get_css_attribute_of_element(locators.parse_and_get(locator_path), attribute)
    assert_that(actual_value).is_equal_to(value)


@given(parsers.re("The css attribute '(?P<attribute>.*)' of element '(?P<locator_path>.*)' is not the value '(?P<value>.*)'"))
def check_css_property_is_not(attribute, selenium_generics: SeleniumGenerics, locators: Locators, locator_path, value):
    actual_value = selenium_generics.get_css_attribute_of_element(locators.parse_and_get(locator_path), attribute)
    assert_that(actual_value).is_not_equal_to(value)


@given(parsers.re("The cookie '(?P<name>.*)' contains the value '(?P<value>.*)'"))
def check_cookie_content(selenium, name, value):
    assert_that(selenium.get_cookie(name)).contains(value)


@given(parsers.re("The cookie '(?P<name>.*)' does not contain the value '(?P<value>.*)'"))
def check_cookie_content_is_not(selenium, name, value):
    assert_that(selenium.get_cookie(name)).does_not_contain(value)


@given(parsers.re("The cookie '(?P<name>.*)' exists"))
def check_cookie_exists(selenium, name):
    assert_that(selenium.get_cookie(name)).is_equal_to(None)


@given(parsers.re("The cookie '(?P<name>.*)' does not exist"))
def check_cookie_does_not_exist(selenium, name):
    assert_that(selenium.get_cookie(name)).is_not_equal_to(None)


@given(parsers.re("The browser resolution is '(?P<width>.*)' per '(?P<height>.*)'"))
@given(parsers.re("My screen resolution is '(?P<width>.*)' by '(?P<height>.*)' pixels"))
def window_size(selenium, width, height):
    selenium.set_window_size(width, height)


@given(parsers.re("There is just one browser tab open"))
@given(parsers.re("There is just one window open"))
def close_all_but_first_tab(selenium):
    windows = selenium.window_handles
    windows.reverse()
    del windows[-1]
    for window in windows:
        selenium.switch_to_window(window)
        selenium.close()


@given(parsers.re("A alertbox is opened"))
@given(parsers.re("A confirmbox is opened"))
@given(parsers.re("A prompt is opened"))
def check_modal():
    from selenium.webdriver.support import expected_conditions as EC
    assert_that(EC.alert_is_present()).is_true()


@given(parsers.re("A alertbox is not opened"))
@given(parsers.re("A confirmbox is not opened"))
@given(parsers.re("A prompt is not opened"))
def check_modal_not_present():
    from selenium.webdriver.support import expected_conditions as EC
    assert_that(EC.alert_is_present()).is_false()
