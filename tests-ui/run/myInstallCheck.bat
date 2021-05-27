cd ..

python -m pytest -v --gherkin-terminal-reporter --driver Chrome --driver-path ./webdriver/chromedriver --capability headless True --variables webdriver/capabilities_web.json --variables i18n.json --variables variables.json --tags "installation_check"

