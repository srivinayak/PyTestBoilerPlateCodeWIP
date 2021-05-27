import os

from assertpy import assert_that
from pytest_bdd import scenarios, then

from step_definitions.steps_given import *
from step_definitions.steps_then import *
from step_definitions.steps_when import *
from step_definitions.steps_custom import *


scenarios('../features/installation_check/cases.feature')


@then("root folder structure is correct")
def check_root_folder():
    assert_that(os.path.isfile('./.editorconfig')).is_true()
    assert_that(os.path.isfile('./.gitignore')).is_true()
    assert_that(os.path.isfile('./.local.env')).is_true()
    assert_that(os.path.isfile('./.pylintrc')).is_true()
    assert_that(os.path.isfile('./conftest.py')).is_true()
    assert_that(os.path.isfile('./i18n.json')).is_true()
    assert_that(os.path.isfile('./install.sh')).is_true()
    assert_that(os.path.isfile('./pytest.ini')).is_true()
    assert_that(os.path.isfile('./README.md')).is_true()
    assert_that(os.path.isfile('./requirements.txt')).is_true()
    assert_that(os.path.isfile('./variables.json')).is_true()


@then("features folder structure is correct")
def check_feature_folder():
    assert_that(os.path.isdir('./features')).is_true()
    assert_that(os.path.isdir('./features/codeless')).is_true()
    assert_that(os.path.isdir('./features/installation_check')).is_true()


@then("page_objects folder structure is correct")
def check_page_objects_folder():
    assert_that(os.path.isdir('./page_objects')).is_true()
    assert_that(os.path.isfile('./page_objects/base_component.py')).is_true()
    assert_that(os.path.isfile('./page_objects/base_page.py')).is_true()
    assert_that(os.path.isfile('./page_objects/selenium_generics.py')).is_true()


@then("screenshots folder structure is correct")
def check_screenshots_folder():
    assert_that(os.path.isdir('./screenshots')).is_true()
    assert_that(os.path.isdir('./screenshots/base')).is_true()


@then("scripts folder structure is correct")
def check_scripts_folder():
    assert_that(os.path.isdir('./scripts')).is_true()
    assert_that(os.path.isdir('./scripts/installation_scripts')).is_true()


@then("step_definitions folder structure is correct")
def check_step_definitions_folder():
    assert_that(os.path.isdir('./step_definitions')).is_true()
    assert_that(os.path.isfile('./step_definitions/steps_custom.py')).is_true()
    assert_that(os.path.isfile('./step_definitions/steps_given.py')).is_true()
    assert_that(os.path.isfile('./step_definitions/steps_then.py')).is_true()
    assert_that(os.path.isfile('./step_definitions/steps_when.py')).is_true()
    assert_that(os.path.isfile('./step_definitions/test_installation_check.py')).is_true()


@then("test_data folder structure is correct")
def check_test_data_folder():
    assert_that(os.path.isdir('./test_data')).is_true()
    assert_that(os.path.isfile('./test_data/faker_data.py')).is_true()


@then("utils folder structure is correct")
def check_utils_folder():
    assert_that(os.path.isdir('./utils')).is_true()
    assert_that(os.path.isfile('./utils/env_variables.py')).is_true()
    assert_that(os.path.isfile('./utils/gherkin_utils.py')).is_true()
    assert_that(os.path.isfile('./utils/utils.py')).is_true()


@then("webdriver folder structure is correct")
def check_webdriver_folder():
    assert_that(os.path.isdir('./webdriver')).is_true()
    assert_that(os.path.isfile('./webdriver/capabilities_android_app.json')).is_true()
    assert_that(os.path.isfile('./webdriver/capabilities_android_web.json')).is_true()
    assert_that(os.path.isfile('./webdriver/capabilities_ios_app.json')).is_true()
    assert_that(os.path.isfile('./webdriver/capabilities_ios_web.json')).is_true()
    assert_that(os.path.isfile('./webdriver/capabilities_web.json')).is_true()
    assert_that(os.path.isfile('./webdriver/capabilities_web_local.json')).is_true()
    assert_that(os.path.isfile('./webdriver/custom_commands.py')).is_true()
    assert_that(os.path.isfile('./webdriver/local_storage.py')).is_true()
