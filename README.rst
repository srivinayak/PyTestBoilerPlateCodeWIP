************************************************
Version 2.1 - Python Test Automation Boilerplate
************************************************

.. contents:: **Table of Contents**
    :depth: 2

Description
===========
Version 2.1 is the unsupported version of the Python Test Automation Boilerplate.

It contains specific third party features to enable you to create tests within your local projects.

Installation
============

Installing for the First Time
-----------------------------

See `Cloning the Test Boilerplate Repository`_ within the `DSE Quality & Test`_ SharePoint site.

When cloning this boilerplate, ensure you choose `v2.1`_ rather than a different version. 

Upgrading From Version 2.0 to 2.1
---------------------------------

See `Upgrading your version of the boilerplate`_.


Features
========

- Powerful test library to support complex functional testing
   - Using `pytest`_
- `Cucumber`_ integration to employ Behavior-Driven Development (BDD)
   - Using `pytest-bdd`_
- 100+ predefined Cucumber StepDefinitions
   - Using `predefined_steps`_
- Easily handle flaky tests by re-running them
   - Using `pytest-rerunfailures`_
- Selenium integration, industry de-facto in web automation
   - Using `pytest-selenium`_
- Easily manage webdriver versions on your machine
   - Using `webdrivermanager`_
- Enhanced Selenium functionality with custom commands. Take full page screenshots on multiple browsers/devices. Screenshots comparison and Visual Regression testing
   - Using `pytest-selenium-enhancer`_
- Multi-Browser and Multi-device support integration
   - Using `BrowserStack`_
- Mobile devices testing capabilities
   - Using `Appium`_
- Simple assertions using fluent API
   - Using `assertpy`_
- TestRail integration
   - Using `pytest-testrail-client`_
- API testing with an elegant and simple HTTP library
   - Using `requests`_

Resources
=========

- `Changelog`_

- `GitHub Code`_

- `Working with this boilerplate`_

- `Reporting issues with this boilerplate`_



.. _Digital Solutions & Enablement: https://teams.microsoft.com/l/team/19%3a983bec845cee4b08a1023f7b8ece093e%40thread.skype/conversations?groupId=5f70f02d-fc1d-41d0-ab99-2043005d8107&tenantId=7a916015-20ae-4ad1-9170-eefd915e9272
.. _DSE Quality & Test: https://pfizer.sharepoint.com/sites/DSEQualityTest
.. _Cloning the Test Boilerplate Repository: https://pfizer.sharepoint.com/sites/DSEQualityTest/SitePages/Cloning-the-test-boilerplate-repository.aspx
.. _Upgrading your version of the boilerplate: https://pfizer.sharepoint.com/sites/DSEQualityTest/SitePages/Upgrading-your-version-of-the-boilerplate.aspx

.. _v1.1: https://github.com/pfizer/python-test-automation-boilerplate/tree/release/1.1
.. _v2.0: https://github.com/pfizer/python-test-automation-boilerplate/tree/release/2.0
.. _v2.1: https://github.com/pfizer/python-test-automation-boilerplate/tree/release/2.1

.. _pytest: http://pytest.org
.. _Python 3.7.8: https://www.python.org/downloads/release/python-378/
.. _Git for Windows: https://gitforwindows.org/
.. _installation_scripts.zip: https://github.com/pfizer/python-test-automation-boilerplate/blob/release/2.0/installation_scripts.zip

.. _Cucumber: https://cucumber.io/
.. _pytest-bdd: https://pytest-bdd.readthedocs.io/en/latest/
.. _predefined_steps: https://github.com/pfizer/python-test-automation-boilerplate/blob/release/2.0/docs/GHERKIN_STEPS.rst
.. _pytest-rerunfailures: https://pypi.org/project/pytest-rerunfailures/
.. _pytest-selenium: https://pytest-selenium.readthedocs.io/en/latest/
.. _webdrivermanager: https://pypi.org/project/webdrivermanager/
.. _pytest-selenium-enhancer: https://pypi.org/project/pytest-selenium-enhancer/
.. _Appium: http://appium.io/docs/en/about-appium/intro/?lang=en
.. _assertpy: https://github.com/assertpy/assertpy
.. _pytest-testrail-client: https://pypi.org/project/pytest-testrail-client/
.. _requests: https://requests.readthedocs.io/en/master/
.. _BrowserStack: https://browserstack.com

.. _Changelog: https://github.com/pfizer/python-test-automation-boilerplate/blob/master/docs/CHANGELOG.rst
.. _GitHub Code: https://github.com/pfizer/python-test-automation-boilerplate/tree/release/2.1  
.. _Working with this boilerplate: https://pfizer.sharepoint.com/sites/DSEQualityTest/SitePages/Working-with-the-Python-Test-Automation-Boilerplate.aspx
.. _Reporting issues with this boilerplate: https://pfizer.sharepoint.com/sites/DSEQualityTest/SitePages/Reporting-issues-with-the-boilerplate.aspx
