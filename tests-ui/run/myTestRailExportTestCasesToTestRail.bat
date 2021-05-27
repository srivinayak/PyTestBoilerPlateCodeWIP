cd ..

rem python -m pytest -v --pytest-testrail-export-test-cases --pytest-testrail-feature-files-relative-path "features/regression/pect_tc013.feature"
rem python -m pytest -v --pytest-testrail-export-test-cases --pytest-testrail-feature-files-relative-path=features\\regression\\pect_tc013.feature

rem python -m pytest -v --gherkin-terminal-reporter --driver Firefox --driver-path ./webdriver/geckodriver --capability headless False --variables webdriver/capabilities_web.json --variables i18n.json --variables variables.json --tags "pect_tc013" --pytest-testrail-export-test-cases --pytest-testrail-feature-files-relative-path "./features/regression/pect_tc013.feature"

python -m pytest -v --pytest-testrail-export-test-cases --pytest-testrail-feature-files-relative-path features/regression/pect_tc013.feature
