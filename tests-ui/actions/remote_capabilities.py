from selenium import webdriver

#import utilities


class MyRemoteWebDriver:
    def __init__(self):
        pass

    def remote_browser_webdriver(self):
        #mystep = utilities.config_utils.get_My_Config()
        username = "vinaysrinivasan2"
        accessKey = "ryyF3o417XFGPFqrxwpA"
        BROWSERSTACK_URL = 'https://'+username+':'+accessKey+'@hub-cloud.browserstack.com/wd/hub'
        return BROWSERSTACK_URL


    def remote_windows_chrome_driver(self):
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

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver


    def remote_windows_firefox_driver(self):
        timeouts = {
            'implicit': 10,
            'pageLoad': 300000,
            'script': 30000
        }

        desired_capabilities = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'Firefox',
            'browser_version': '86.0',
            'networkConnectionEnabled': 'true',
            'TIMEOUT': timeouts,
            'name': "Remote PECT-TestAutomation WebDriver Test",
            'build': "PECT-TA-BSA-Build-001"
        }

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver


    def remote_windows_edge_driver(self):
        timeouts = {
            'implicit': 10,
            'pageLoad': 300000,
            'script': 30000
        }

        desired_capabilities = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'edge',
            'browser_version': '88.0',
            'networkConnectionEnabled': 'true',
            "browserstack.use_w3c": "true",
            "browserstack.selenium_version": "3.141.59",
            'TIMEOUT': timeouts,
            'name': "Remote PECT-TestAutomation WebDriver Test",
            'build': "PECT-TA-BSA-Build-001"
        }

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver


    def remote_windows_ie11_driver(self):
        timeouts = {
            'implicit': 10,
            'pageLoad': 300000,
            'script': 30000
        }

        desired_capabilities = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'ie',
            'browser_version': '11.0',
            'networkConnectionEnabled': 'true',
            "browserstack.use_w3c": "true",
            "browserstack.selenium_version": "3.141.59",
            "browserstack.ie.arch": "x32",
            "browserstack.ie.driver": "3.141.59",
            'TIMEOUT': timeouts,
            'name': "Remote PECT-TestAutomation WebDriver Test",
            'build': "PECT-TA-BSA-Build-001"
        }

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver


    def remote_iphone_browser_driver(self):

        timeouts = {
            'implicit': 10,
            'pageLoad': 300000,
            'script': 30000
        }

        desired_capabilities = {
            'browserstack.idleTimeout': '300',
            'safariInitialUrl': '',
            'networkConnectionEnabled': 'true',
            '"newCommandTimeout': '10',
            'browserName': 'iPhone',
            'device': 'iPhone XS',
            'realMobile': 'true',
            'os_version': '14',
            'name': "Remote PECT-TestAutomation WebDriver Test",
            'build': "PECT-TA-BSA-Build-001"
        }

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver


    def remote_android_browser_driver(self):
        timeouts = {
            'implicit': 10,
            'pageLoad': 300000,
            'script': 30000
        }
        desired_capabilities = {
            'browserstack.idleTimeout': '300',
            'networkConnectionEnabled': 'true',
            'newCommandTimeout': '15',
            'TIMEOUT': timeouts,
            'acceptInsecureCerts': 'true',
            '--disable-features': 'None',
            'browserName': 'android',
            'device': 'Samsung Galaxy S21',
            'realMobile': 'true',
            'os_version': '11.0',
            'name': "Remote PECT-TestAutomation WebDriver Test",
            'build': "PECT-TA-BSA-Build-001"
        }

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver


    def remote_mac_os_safari_browser_driver(self):
        timeouts = {
            'implicit': 10,
            'pageLoad': 300000,
            'script': 30000
        }

        desired_capabilities = {
            'os': 'OS X',
            'os_version': 'Big Sur',
            'browserstack.idleTimeout': '300',
            '"newCommandTimeout': '10',
            'networkConnectionEnabled': 'true',
            'TIMEOUT': timeouts,
            'browser': 'safari',
            'browser_version': '14.0',
            'safariInitialUrl': "",
            'name': "Remote PECT-TestAutomation WebDriver Test",
            'build': "PECT-TA-BSA-Build-001"
        }

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver


    def remote_mac_os_chrome_browser_driver(self):
        timeouts = {
            'implicit': 10,
            'pageLoad': 300000,
            'script': 30000
        }

        desired_capabilities = {
            'os': 'OS X',
            'os_version': 'Big Sur',
            'networkConnectionEnabled': 'true',
            'TIMEOUT': timeouts,
            'browser': 'Chrome',
            'browser_version': '80',
            'name': "Remote PECT-TestAutomation WebDriver Test",
            'build': "PECT-TA-BSA-Build-001"
        }

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver


    def remote_mac_os_firefox_browser_driver(self):
        timeouts = {
            'implicit': 10,
            'pageLoad': 300000,
            'script': 30000
        }

        desired_capabilities = {
            'os': 'OS X',
            'os_version': 'Big Sur',
            'browser': 'Firefox',
            'browser_version': '86.0',
            'networkConnectionEnabled': 'true',
            'TIMEOUT': timeouts,
            'name': "Remote PECT-TestAutomation WebDriver Test",
            'build': "PECT-TA-BSA-Build-001"
        }

        driver = webdriver.Remote(command_executor=self.remote_browser_webdriver(), desired_capabilities=desired_capabilities)
        return driver

