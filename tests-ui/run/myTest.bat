cd ..


rem python -m pytest -v --gherkin-terminal-reporter --driver Chrome --driver-path ./webdriver/chromedriver --capability headless False --variables webdriver/capabilities_web.json --variables i18n.json --variables variables.json --tags "pect_tc016"
rem python -m pytest -v --gherkin-terminal-reporter --driver Firefox --driver-path ./webdriver/geckodriver --capability headless False --variables webdriver/capabilities_web.json --variables i18n.json --variables variables.json --tags "pect_tc003"
python -m pytest -v --gherkin-terminal-reporter --driver BrowserStack --capability headless False --variables webdriver/capabilities_web.json --variables i18n.json --variables variables.json --tags "pect_tc003"

