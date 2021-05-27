from pytest_bdd import when, parsers
from pytest_selenium_enhancer import CustomWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.locators import Locators


@when(parsers.re("I set the locale for locators to '(?P<locale>.*)'"))
@when(parsers.re("I set the language for locators to '(?P<locale>.*)'"))
def set_locale(locators: Locators, locale):
    locators.set_locale(locale)


@when(parsers.re("I click on '(?P<locator_path>.*)'"))
def click_element(selenium, locators: Locators, locator_path):
    selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)).click()


@when(parsers.re("I double click on '(?P<locator_path>.*)'"))
@when(parsers.re("I doubleclick on '(?P<locator_path>.*)'"))
def dbl_click_element(selenium, locators: Locators, locator_path):
    element = selenium.find_element(By.XPATH, locators.parse_and_get(locator_path))
    ActionChains(selenium).double_click(element).perform()


@when(parsers.re("I programmatic click on '(?P<locator_path>.*)'"))
def js_click_element(selenium, locators: Locators, locator_path):
    element = selenium.find_element(By.XPATH, locators.parse_and_get(locator_path))
    selenium.execute_script('arguments[0].click();', element)


@when(parsers.re("I add text '(?P<text>.*)' to field '(?P<locator_path>.*)'"))
def add_element_value(selenium, text, locators: Locators, locator_path):
    element = selenium.find_element(By.XPATH, locators.parse_and_get(locator_path))
    actual_text = element.get_attribute('value')
    element.send_keys(actual_text + text)


@when(parsers.re("I set text '(?P<text>.*)' to field '(?P<locator_path>.*)'"))
def set_element_value(selenium, text, locators: Locators, locator_path):
    print(locator_path)
    element = selenium.find_element(By.XPATH, locators.parse_and_get(locator_path))
    element.send_keys(text)


@when(parsers.re("I clear text from field '(?P<locator_path>.*)'"))
def set_add_element_value(selenium, locators: Locators, locator_path):
    element = selenium.find_element(By.XPATH, locators.parse_and_get(locator_path))
    element.clear()


@when(parsers.re("I drag and drop element '(?P<source>.*)' to element '(?P<target>.*)'"))
def drag_and_drop_element(selenium, locators: Locators, source, target):
    source_elem = selenium.find_element(By.XPATH, locators.parse_and_get(source))
    target_elem = selenium.find_element(By.XPATH, locators.parse_and_get(target))

    action = ActionChains(selenium)
    action.drag_and_drop(source_elem, target_elem).perform()


@when(parsers.re("I pause for '(?P<time>.*)' s"))
def pause_execution(selenium, time):
    CustomWait(selenium).static_wait(int(time))


@when("I fetch existing cookies from the site")
def fetch_cookies(selenium):
    selenium.get_cookies()


@when(parsers.re("I update the value of newly added cookie '(?P<name>.*)' with '(?P<value>.*)' for path '(?P<path>.*)'"))
@when(parsers.re("I set the cookie '(?P<name>.*)' with value '(?P<value>.*)' for path '(?P<path>.*)'"))
def check_cookie_content(selenium, name, value, path='/'):
    selenium.add_cookie({"name": name, "value": value, "path": path})


@when(parsers.re("I delete the cookie '(?P<name>.*)'"))
def check_cookie_content(selenium, name):
    selenium.delete_cookie(name)


@when(parsers.re("I press '(?P<key>.*)'"))
def press_button(selenium, key):
    ActionChains(selenium).send_keys(key).perform()


@when(parsers.re("I accept popup prompt"))
@when(parsers.re("I accept popup alertbox"))
@when(parsers.re("I accept popup confirmbox"))
def accept_modal(selenium):
    selenium.switch_to().alert().accept()


@when(parsers.re("I dismiss popup prompt"))
@when(parsers.re("I dismiss popup alertbox"))
@when(parsers.re("I dismiss popup confirmbox"))
def dismiss_modal(selenium):
    selenium.switch_to().alert().dismiss()


@when(parsers.re("I enter (?P<text>.*) into popup alertbox"))
@when(parsers.re("I enter (?P<text>.*) into popup confirmbox"))
@when(parsers.re("I enter (?P<text>.*) into popup prompt"))
def check_modal(selenium, text):
    selenium.switch_to().alert().send_keys(text)


@when(parsers.re("I scroll to element '(?P<locator_path>.*)'"))
def scroll_to_element(selenium, locators: Locators, locator_path):
    element = selenium.find_element(By.XPATH, locators.parse_and_get(locator_path))
    script = 'arguments[0].scrollIntoView({block: "center", inline: "center"})'
    selenium.execute_script(script, element)


@when(parsers.re("I close the last opened window"))
@when(parsers.re("I close the last opened tab"))
def close_last_opened_window(selenium):
    windows = selenium.window_handles
    selenium.switch_to_window(windows[-1])
    selenium.close()


@when(parsers.re("I focus the last opened window"))
@when(parsers.re("I focus the last opened tab"))
def switch_to_last(selenium):
    windows = selenium.window_handles
    selenium.switch_to_window(windows[-1])


@when(parsers.re("I select the option at index '(?P<index>.*)' element '(?P<locator_path>.*)'"),
      converters=dict(index=int))
def select_option_by_index(selenium, index: int, locators: Locators, locator_path):
    select = Select(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)))
    select.select_by_index(index)


@when(parsers.re("I select the option '(?P<option>.*)' by value for element '(?P<locator_path>.*)'"))
def select_option_by_value(selenium, option, locators: Locators, locator_path):
    select = Select(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)))
    select.select_by_value(option)


@when(parsers.re("I select the option '(?P<option>.*)' by visible text for element '(?P<locator_path>.*)'"))
def select_option_by_visible_text(selenium, option, locators: Locators, locator_path):
    select = Select(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)))
    select.select_by_visible_text(option)


@when(parsers.re("I deselect the option at index '(?P<index>.*)' element '(?P<locator_path>.*)'"),
      converters=dict(index=int))
def deselect_option_index(selenium, index: int, locators: Locators, locator_path):
    select = Select(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)))
    select.deselect_by_index(index)


@when(parsers.re("I deselect the option '(?P<option>.*)' by value for element '(?P<locator_path>.*)'"))
def deselect_option_by_value(selenium, option, locators: Locators, locator_path):
    select = Select(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)))
    select.deselect_by_value(option)


@when(parsers.re("I deselect the option '(?P<option>.*)' by visible text for element '(?P<locator_path>.*)'"))
def deselect_option_by_visible_text(selenium, option, locators: Locators, locator_path):
    select = Select(selenium.find_element(By.XPATH, locators.parse_and_get(locator_path)))
    select.deselect_by_visible_text(option)


@when(parsers.re("I move to element '(?P<locator_path>.*)' with offset '(?P<x>.*)' '(?P<y>.*)'"))
def move_to_element_by_offset(selenium, locators: Locators, locator_path, x, y):
    element = selenium.find_element(By.XPATH, locators.parse_and_get(locator_path))
    ActionChains(selenium).move_to_element_with_offset(element, int(x), int(y))


@when(parsers.re("I move to element '(?P<locator_path>.*)'"))
def move_to_element_by_offset(selenium, locators: Locators, locator_path):
    element = selenium.find_element(By.XPATH, locators.parse_and_get(locator_path))
    ActionChains(selenium).move_to_element(element)
