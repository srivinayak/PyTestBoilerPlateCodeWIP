cd ..

rem python -m pytest tr_configs=testrail.cfg --pytest-testrail-export-test-results --pytest-testrail-test-plan-id 1 --pytest-testrail-test-configuration-name "TR-C7"
rem python -m pytest --pytest-testrail-export-test-results --pytest-testrail-test-configuration-name TR-C7
python -m pytest --gherkin-terminal-reporter --driver BrowserStack --capability headless False --variables webdriver/capabilities_web.json --variables i18n.json --variables variables.json --tags "pect_tc013" -v --testrail --tr-config=testrail.cfg --pytest-testrail-export-test-results --testrail-project-id 1 --pytest-testrail-test-plan-id 1 --pytest-testrail-test-configuration-name "TR-C7"

