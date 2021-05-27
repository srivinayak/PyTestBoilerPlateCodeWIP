# pylint: disable=invalid-name
# pylint: disable=protected-access
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
import json
import logging
import pytest
from collections import defaultdict
from typing import List
from logging.config import fileConfig
from _pytest.config import Config
from _pytest.python import Metafunc
from cucumber_tag_expressions import parse
from pytest_selenium import pytest_selenium, driver
from selenium.webdriver.remote.webdriver import WebDriver
from os import path

import actions
from actions.browser import BrowserActions
from actions.remote_capabilities import MyRemoteWebDriver
from page_objects.selenium_generics import SeleniumGenerics
from utils.env_variables import EnvVariables
from utils.locators import Locators
from utils.utils import initialize_screenshot_dirs
from webdriver.custom_commands import my_custom_commands

logger = logging.getLogger(__name__)


browser_configs = []
test_ids: List[str] = []

#BROWSERSTACK_USER = "vinaysrinivasan2"
#BROWSERSTACK_ACCESS_KEY = "ryyF3o417XFGPFqrxwpA"
global session
global selenium
global driver


def pytest_configure(config: Config):
    config.option.keyword = 'automated'
    config.option.markexpr = 'not not_in_scope'
    pytest.globalDict = defaultdict()
    pytest.scenarioDict = defaultdict()
    mat_option = config.getoption("--device-matrix", default=None)
    if mat_option:
        with open(str(mat_option), 'r') as mat:
            matrix = json.load(mat)
            browser_configs.extend(matrix)


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en',
                     type=str,
                     help='Application language')
    parser.addoption('--tags',
                     metavar="str",
                     help='Will filter tests by given tags')
    parser.addoption('--device-matrix',
                     metavar="str",
                     help='The different configurations against which the test would be run')


def pytest_collection_modifyitems(config, items):
    if 'pytest_testrail_export_test_cases' not in config.option \
        or config.option.pytest_testrail_export_test_cases is False:
        raw_tags = config.option.tags
        if raw_tags is not None:
            for item in items:
                item_tags = [marker.name for marker in item.own_markers]
                if not parse(raw_tags).evaluate(item_tags):
                    item.add_marker(pytest.mark.not_in_scope)


#@pytest.fixture(scope='session', autouse=True)
def pytest_sessionstart(session):
    initialize_screenshot_dirs(session.config.rootdir)
    if browser_configs:
        # delete and overwrite the locally defined selenium fixture if we have configs from file
        global selenium
        global driver
        tr_configs = 0

        @pytest.fixture(scope='session')
        def selenium(multi_browser):
            #multi_browser = actions.remote_capabilities.MyRemoteWebDriver().remote_windows_chrome_driver()
            #actions.remote_capabilities.MyRemoteWebDriver().remote_windows_firefox_driver()
            return multi_browser

    if path.exists('logging.cfg'):
        logging.config.fileConfig("logging.cfg", disable_existing_loggers=False)
        logging.getLogger(__name__)


#@pytest.fixture(scope='session', autouse=True)
def pytest_bdd_before_scenario(feature, scenario):
    pytest.scenarioDict = defaultdict()
    logger.info('****** Started executing Scenario: "{scenario.name}" from Feature: "{feature.name}" ******'.
                format(scenario=scenario, feature=feature))
    try:
        driver.maximize_window()
        yield driver
    except Exception as e00:
        pass


#@pytest.fixture(scope='session', autouse=True)
def pytest_bdd_after_scenario(feature, scenario):
    pytest.scenarioDict = defaultdict()
    logger.info('****** Scenario: "{scenario.name}" execution completed for Feature: "{feature.name}"******'.
                format(scenario=scenario, feature=feature))


#@pytest.fixture(scope='session', autouse=True)
def pytest_sessionfinish(session, exitstatus):
#def pytest_bdd_after_feature(feature, scenario):
    try:
        del selenium
    except Exception as e1:
        pass

    try:
        driver.close()
    except Exception as e2:
        pass

    try:
        driver.quit()
    except Exception as e3:
        pass


    try:
        del driver
    except Exception as e4:
        pass



def pytest_bdd_step_error(feature, scenario, step, exception):
    logger.error(f'****** While running Feature: "{feature.name}"; Step: "{step.name}" FAILED from Scenario: '
                 f'"{scenario.name}" with exception: {exception} ******')


def pytest_bdd_after_step(feature, scenario, step):
    logger.info('****** Step: "{step.name}" PASSED from Scenario:" {scenario.name} " and Feature: '
                '"{feature.name}" ******'.format(step=step, scenario=scenario, feature=feature))


def pytest_generate_tests(metafunc: Metafunc):
    if browser_configs:
        if not test_ids:
            # Generate test IDs from the configs
            for config in browser_configs:
                browser_name = config.get("browser", "").strip().lower()
                browser_version = config.get("browser_version", "").strip().lower()
                resolution = config.get("resolution", "").strip().lower()
                device = config.get("device", "").strip().lower()
                real_device = ""
                if device:
                    real_device = \
                        "realDevice" if device and config.get("real_mobile", "").strip().lower() == "true" \
                            else "emulated"
                os = config.get("os", "").strip().lower()
                os_version = config.get("os_version", "").strip().lower()
                orientation = config.get("deviceOrientation", "").strip().lower()

                field_list: List[str] = \
                    [device, os, os_version, real_device, browser_name, browser_version, resolution, orientation]
                id_str = "-".join([field for field in field_list if field])

                test_ids.append(id_str)

        metafunc.parametrize("custom_browser_config", browser_configs, ids=test_ids, indirect=True)


def mycaps():
    timeouts = {
        'implicit': 10000,
        'pageLoad': 300000,
        'script': 300000
    }

    desired_capabilities = {
        'os': 'Windows',
        'os_version': '10',
        "browserstack.idleTimeout": 30,
        'acceptInsecureCerts': 'true',
        'networkConnectionEnabled': 'true',
        'TIMEOUT': timeouts,
        'browser': 'Chrome',
        'browser_version': '80',
        "browserstack.seleniumLogs": 'true',
        "browserstack.console": 'errors',
        'name': "Remote PECT-TestAutomation WebDriver Test",
        'build': "PECT-TA-BSA-Build-001"
    }


@pytest.fixture
#def multi_browser(custom_browser_config, env_variables: EnvVariables) -> WebDriver:
def multi_browser(custom_browser_config, env_variables: EnvVariables):
    #driver = None
    #if(driver == "BrowserStack"):
    ###driver = actions.remote_capabilities.MyRemoteWebDriver().remote_windows_chrome_driver()
        #driver = actions.remote_capabilities.MyRemoteWebDriver().remote_windows_firefox_driver()

    if custom_browser_config.get("local", "").strip().lower() == "true":
        browser_given = custom_browser_config["browser"]
        driver_path = custom_browser_config["driver_path"]
        driver_class = pytest_selenium.SUPPORTED_DRIVERS[browser_given]
        driver = driver_class(driver_path)
        resolution = [int(num_str.strip()) for num_str in custom_browser_config["resolution"].split('x')]
        driver.set_window_size(resolution[0], resolution[1])

    else:
        driver_class = pytest_selenium.SUPPORTED_DRIVERS["BrowserStack"]
        driver = driver_class(
            command_executor="https://{env_variables.get('BROWSERSTACK_USER')}:{env_variables.get('BROWSERSTACK_ACCESS_KEY')}@hub-cloud.browserstack.com/wd/hub",
            ##command_executor=f"https://"+ BROWSERSTACK_USER + ":" + BROWSERSTACK_ACCESS_KEY + "@hub-cloud.browserstack.com/wd/hub",
            desired_capabilities=custom_browser_config
            ##desired_capabilities=mycaps().desired_capabilities
        )
        #if 'os' in custom_browser_config:
        driver.maximize_window()

    yield driver

    #driver.quit()


@pytest.fixture
def selenium(selenium, selenium_patcher, variables):
    my_custom_commands()
    selenium.delete_all_cookies()
    return selenium


@pytest.fixture
def selenium_generics(selenium) -> SeleniumGenerics:
    return SeleniumGenerics(selenium)


@pytest.fixture
def browser(selenium) -> BrowserActions:
    return BrowserActions(selenium)


@pytest.fixture
def chrome_options(chrome_options, variables):
    if 'headless' in variables['capabilities'] and variables['capabilities']['headless'] == 'True':
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--hide-scrollbars')
    return chrome_options


@pytest.fixture
def capabilities(capabilities):
    if 'browser' in capabilities and capabilities['browser'] in ['Edge', 'MicrosoftEdge']:
        capabilities['browserstack.edge.enablePopups'] = 'true'
    if 'browser' in capabilities and capabilities['browser'] in ['safari', 'Safari']:
        capabilities['browserstack.safari.enablePopups'] = 'true'
    return capabilities


# needs to be session scoped with auto use enabled for this to show up
# in the list of fixtures in the generate tests hook
@pytest.fixture(scope='session', autouse=True)
def custom_browser_config(request):
    try:
        return request.param
    except:
        return None


@pytest.fixture(scope='session')
def language(request):
    config = request.config
    language = config.getoption('language')
    if language is not None:
        return language
    return None


@pytest.fixture(scope='session')
def project_dir(request, pytestconfig) -> str:
    path_str = request.session.config.known_args_namespace.confcutdir
    # the value above is None in some cases(not sure why). so, adding the fallback below
    return path_str if path_str else str(pytestconfig.rootdir)


@pytest.fixture(scope='session', autouse=True)
def locators(project_dir) -> Locators:
    return Locators(f"{project_dir}/locators.json")


@pytest.fixture(scope='session')
def env_variables(project_dir):
    env_vars_file_path = "%s/.local.env" % project_dir
    return EnvVariables(env_vars_file_path)


@pytest.fixture(scope='session')
def log():
    # Get the top-level logger object
    log = logging.getLogger()

    # make it print to the console.
    console = logging.StreamHandler()
    log.addHandler(console)
    return log
