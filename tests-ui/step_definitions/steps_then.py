from assertpy import assert_that
from pytest_bdd import then, parsers
from pytest_selenium_enhancer import CustomWait
from selenium.webdriver.common.by import By

from page_objects.selenium_generics import SeleniumGenerics
from utils.locators import Locators


@then(parsers.re("I expect that the title is '(?P<title>.*)'"))
def check_title_is(selenium, title):
    assert_that(selenium.title).is_equal_to(title)


@then(parsers.re("I expect that the title is not '(?P<title>.*)'"))
def check_title_is_not(selenium, title):
    assert_that(selenium.title).is_not_equal_to(title)


@then(parsers.re("I expect that the title contains '(?P<title>.*)'"))
def check_title_contains(selenium, title):
    assert_that(selenium.title).contains(title)


@then(parsers.re("I expect that the title does not contain '(?P<title>.*)'"))
def check_title_not_contains(selenium, title):
    assert_that(selenium.title).does_not_contain(title)


@then(parsers.re("I expect that element '(?P<locator_path>.*)' appears exactly '(?P<occurrence_count>.*)' times"))
def check_element_exists(selenium, locators: Locators, locator_path, occurrence_count):
    locator = locators.parse_and_get(locator_path)
    assert_that(len(selenium.find_elements(By.XPATH, locator))).is_equal_to(int(occurrence_count))


@then(parsers.re("I expect that element '(?P<locator_path>.*)' does not appear exactly '(?P<occurrence_count>.*)' times"))
def check_element_not_exists(selenium, locators: Locators, locator_path, occurrence_count):
    locator = locators.parse_and_get(locator_path)
    assert_that(len(selenium.find_elements(By.XPATH, locator))).is_not_equal_to(int(occurrence_count))


@then(parsers.re("I expect that element '(?P<locator_path>.*)' is displayed"))
def element_displayed(selenium, locators: Locators, locator_path):
    assert_that(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)).is_displayed()).is_true()


@then(parsers.re("I expect that element '(?P<locator_path>.*)' is not displayed"))
def element_not_displayed(selenium, locators: Locators, locator_path):
    assert_that(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)).is_displayed()).is_false()


@then(parsers.re("I expect that element '(?P<locator_path>.*)' becomes visible"))
def wait_for_displayed(selenium, locators: Locators, locator_path):
    CustomWait(selenium).wait_for_element_visible(value=locators.parse_and_get(locator_path))


@then(parsers.re("I expect that element '(?P<locator_path>.*)' becomes invisible"))
def wait_for_not_displayed(selenium, locators: Locators, locator_path):
    CustomWait(selenium).wait_for_element_not_visible(value=locators.parse_and_get(locator_path))


@then(parsers.re("I expect that element '(?P<locator_path>.*)' is within the viewport"))
def check_within_viewport(selenium, locators: Locators, locator_path):
    assert_that(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)).is_in_viewport()).is_true()


@then(parsers.re("I expect that element '(?P<locator_path>.*)' is not within the viewport"))
def check_within_viewport(selenium, locators: Locators, locator_path):
    assert_that(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)).is_in_viewport()).is_false()


@then(parsers.re("I expect that element '(?P<locator_path>.*)' exists"))
def check_is_existing(selenium, locators: Locators, locator_path):
    CustomWait(selenium).wait_for_element_present(value=locators.parse_and_get(locator_path))


@then(parsers.re("I expect that element '(?P<locator_path>.*)' does not exist"))
def check_element_not_existing(selenium, locators: Locators, locator_path):
    CustomWait(selenium).wait_for_element_not_visible(value=locators.parse_and_get(locator_path))


@then(parsers.re("I expect that element '(?P<locator_path1>.*)' contains the same text as element'(?P<locator_path2>.*)'$"))
def check_contains_same_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path1, locator_path2):
    actual_text1 = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path1))
    actual_text2 = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path2))
    assert_that(actual_text1).is_equal_to(actual_text2)


@then(parsers.re("I expect that element '(?P<locator_path1>.*)' does not contain the same text as element'(?P<locator_path2>.*)'$"))
def check_does_not_contain_same_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path1, locator_path2):
    actual_text1 = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path1))
    actual_text2 = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path2))
    assert_that(actual_text1).is_not_equal_to(actual_text2)


@then(parsers.re("The button '(?P<locator_path>.*)' text is '(?P<text>.*)'"))
@then(parsers.re("The element '(?P<locator_path>.*)' text is '(?P<text>.*)'"))
def check_element_equals_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).is_equal_to(text)


@then(parsers.re("The button '(?P<locator_path>.*)' text is not '(?P<text>.*)'"))
@then(parsers.re("The element '(?P<locator_path>.*)' text is not '(?P<text>.*)'"))
def check_element_not_equals_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).is_not_equal_to(text)


@then(parsers.re("The trimmed text on button '(?P<locator_path>.*)' is '(?P<text>.*)'"))
@then(parsers.re("The trimmed text on element '(?P<locator_path>.*)' is '(?P<text>.*)'"))
def check_element_equals_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text.strip()).is_equal_to(text)


@then(parsers.re("The trimmed text on button '(?P<locator_path>.*)' is not '(?P<text>.*)'"))
@then(parsers.re("The trimmed text on element '(?P<locator_path>.*)' is not '(?P<text>.*)'"))
def check_element_not_equals_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text.strip()).is_not_equal_to(text)


@then(parsers.re("The button '(?P<locator_path>.*)' contains the text '(?P<text>.*)'"))
@then(parsers.re("The element '(?P<locator_path>.*)' contains the text '(?P<text>.*)'"))
def check_contains_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).contains(text)


@then(parsers.re("The button '(?P<locator_path>.*)' does not contain the text '(?P<text>.*)'"))
@then(parsers.re("The element '(?P<locator_path>.*)' does not contain the text '(?P<text>.*)'"))
def check_not_contains_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, text):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).does_not_contain(text)


@then(parsers.re("The button '(?P<locator_path>.*)' does not contain any text"))
@then(parsers.re("The element '(?P<locator_path>.*)' does not contain any text"))
def check_contains_no_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).matches(r'^$')


@then(parsers.re("The button '(?P<locator_path>.*)' contains any text"))
@then(parsers.re("The element '(?P<locator_path>.*)' contains any text"))
def check_contains_any_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path):
    actual_text = selenium_generics.get_text_from_element(locators.parse_and_get(locator_path))
    assert_that(actual_text).matches(r'(.*?)')


@then(parsers.re("The page url is '(?P<url>.*)'"))
def check_page_url(selenium, url):
    CustomWait.static_wait(2)
    assert_that(selenium.current_url).is_equal_to(url)


@then(parsers.re("The page url is not '(?P<url>.*)'"))
def check_page_url_is_not(selenium, url):
    assert_that(selenium.current_url).is_not_equal_to(url)


@then(parsers.re("The page path is '(?P<url>.*)'"))
@then(parsers.re("The page url contains '(?P<url>.*)'"))
def check_page_url_contains(selenium, url):
    CustomWait.static_wait(2)
    assert_that(selenium.current_url).contains(url)


@then(parsers.re("The page path is not '(?P<url>.*)'"))
@then(parsers.re("The page url does not contain '(?P<url>.*)'"))
def check_page_url_not_contains(selenium, url):
    assert_that(selenium.current_url).does_not_contain(url)


@then(parsers.re("The attribute '(?P<attribute>.*)' of element '(?P<locator_path>.*)' is '(?P<value>.*)'"))
def check_property_is(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, value, attribute):
    actual_value = selenium_generics.get_attribute_of_element(locators.parse_and_get(locator_path), attribute)
    assert_that(actual_value).is_equal_to(value)


@then(parsers.re("The attribute '(?P<attribute>.*)' of element '(?P<locator_path>.*)' is not '(?P<value>.*)'"))
def check_property_is_not(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, value, attribute):
    actual_value = selenium_generics.get_attribute_of_element(locators.parse_and_get(locator_path), attribute)
    assert_that(actual_value).is_not_equal_to(value)


@then(parsers.re("The css attribute '(?P<attribute>.*)' of element '(?P<locator_path>.*)' is '(?P<value>.*)'"))
def check_css_property_is(attribute, selenium_generics: SeleniumGenerics, locators: Locators, locator_path, value):
    actual_value = selenium_generics.get_css_attribute_of_element(locators.parse_and_get(locator_path), attribute)
    assert_that(actual_value).is_equal_to(value)


@then(parsers.re("The css attribute '(?P<attribute>.*)' of element '(?P<locator_path>.*)' is not '(?P<value>.*)'"))
def check_css_property_is_not(attribute, selenium_generics: SeleniumGenerics, locators: Locators, locator_path, value):
    actual_value = selenium_generics.get_css_attribute_of_element(locators.parse_and_get(locator_path), attribute)
    assert_that(actual_value).is_not_equal_to(value)


@then(parsers.re("The element '(?P<locator_path>.*)' is selected"))
def check_element_selected(selenium, locators: Locators, locator_path):
    locator = locators.parse_and_get(locator_path)
    CustomWait(selenium).wait_for_element_visible(value=locator)
    assert_that(selenium.find_element(By.XPATH, locator).is_selected()).is_true()


@then(parsers.re("The element '(?P<locator_path>.*)' is not selected"))
def check_element_not_selected(selenium, locators: Locators, locator_path):
    locator = locators.parse_and_get(locator_path)
    CustomWait(selenium).wait_for_element_visible(value=locator)
    assert_that(selenium.find_element(By.XPATH, locator).is_selected()).is_false()


@then(parsers.re("The element '(?P<locator_path>.*)' is enabled"))
def check_element_enabled(selenium, locators: Locators, locator_path):
    locator = locators.parse_and_get(locator_path)
    CustomWait(selenium).wait_for_element_visible(value=locator)
    assert_that(selenium.find_element(By.XPATH, locator).is_enabled()).is_true()


@then(parsers.re("The element '(?P<locator_path>.*)' is not enabled"))
def check_element_not_enabled(selenium, locators: Locators, locator_path):
    locator = locators.parse_and_get(locator_path)
    CustomWait(selenium).wait_for_element_visible(value=locator)
    assert_that(selenium.find_element(By.XPATH, locator).is_enabled()).is_false()


@then(parsers.re("The url '(?P<url>.*)' is opened in a new tab"))
@then(parsers.re("The url '(?P<url>.*)' is opened in a new window"))
def check_is_opened_in_new_window(selenium, url):
    windows = selenium.window_handles
    window = windows[-1]
    selenium.switch_to_window(window)
    assert_that(selenium.current_url).is_equal_to(url)


@then(parsers.re("A alertbox is opened"))
@then(parsers.re("A confirmbox is opened"))
@then(parsers.re("A prompt is opened"))
def check_modal():
    from selenium.webdriver.support import expected_conditions as EC
    assert_that(EC.alert_is_present()).is_true()


@then(parsers.re("A alertbox is not opened"))
@then(parsers.re("A confirmbox is not opened"))
@then(parsers.re("A prompt is not opened"))
def check_modal_not_present():
    from selenium.webdriver.support import expected_conditions as EC
    assert_that(EC.alert_is_present()).is_false()


@then(parsers.re("There are '(?P<count>.*)' tabs currently opened"), converters=dict(count=int))
@then(parsers.re("There are '(?P<count>.*)' windows currently opened"), converters=dict(count=int))
def check_number_of_tabs(selenium, count: int):
    assert_that(len(selenium.window_handles)).is_equal_to(count)


@then(parsers.re("A new tab is opened"))
@then(parsers.re("A new window is opened"))
def check_new_window(selenium):
    windows = selenium.window_handles
    assert_that(windows.__len__()).is_greater_than(1)


@then(parsers.re("A new tab is not opened"))
@then(parsers.re("A new window is not opened"))
def check_no_new_window(selenium):
    windows = selenium.window_handles
    assert_that(windows.__len__()).is_equal_to(1)


@then("I expect the cookies to be present")
def check_cookies_presence(selenium):
    assert_that(selenium.get_cookies()).is_not_empty()


@then(parsers.re("I expect cookie '(?P<name>.*)' with value '(?P<value>.*)' to be present"))
def check_cookie_presence(selenium, name, value):
    assert_that(selenium.get_cookie(name)).is_not_equal_to(None)
    assert_that(selenium.get_cookie(name)['value']).is_equal_to(value)


@then(parsers.re("I expect the value of newly added cookie '(?P<name>.*)' to be updated with '(?P<value>.*)'"))
def check_cookie_update(selenium, name, value):
    assert_that(selenium.get_cookie(name)['value']).is_equal_to(value)


@then(parsers.re("I expect cookie '(?P<name>.*)' to be deleted"))
def check_cookie_delete(selenium, name):
    assert_that(selenium.get_cookie(name)).is_equal_to(None)
