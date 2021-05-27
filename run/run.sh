#!/bin/sh

python -m pytest -v --gherkin-terminal-reporter --driver Chrome --driver-path ./scripts/chromedriver --capability headless False --variables webdriver/capabilities_web.json --variables i18n.json --variables variables.json --tags "PECT_TC002"