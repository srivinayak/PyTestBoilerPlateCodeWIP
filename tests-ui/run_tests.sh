
# the gherkin tags for tests to be run
TAGS=$1
if [ "$TAGS" = "" ]
then
  TAGS="automated" # the default tags to run
fi

# the app env to run the tests against
BASE_URL=$2
if [ "$BASE_URL" = "" ]
then
  BASE_URL="https://championspfizercom-preview.dev.pfizerstatic.io/" # the default value for base url
fi

HEADLESS=$3
# if we're running inside a GH Actions runner, ignore cmd line arg and force headless mode
if [ "$CI" != "" ]
then
  HEADLESS="True"
elif [ "$HEADLESS" = "" ] || [ "$HEADLESS" = "n" ]
then
  HEADLESS="False"
elif [ "$HEADLESS" = "y" ]
then
  HEADLESS="True"
fi

# determines whether the results would be published to testrail or not
TEST_PLAN=$4
if [ "$TEST_PLAN" = "" ] || [ "$TEST_PLAN" = "n" ]
then
  TEST_PLAN=""
elif [ "$TEST_PLAN" = "y" ]
then
  TEST_PLAN="" # the default testrail test plan id would go here
fi

# number of times to retry failed tests
RETRY=$5
if [ "$RETRY" = "" ]
then
  RETRY=1
fi

# Setting the right driver executable for the platform
case "$(uname)" in
  Darwin*)    PLATFORM_TYPE="macOS"; \
              ;;
  WindowsNT* | MINGW64* ) PLATFORM_TYPE="WINDOWS"; \
              ;;
  *)     PLATFORM_TYPE="LINUX"; \
              ;;
esac

DRIVER_PATH=./scripts/chromedriver
if [ "$PLATFORM_TYPE" == "WINDOWS" ]
then
  DRIVER_PATH=./scripts/chromedriver.exe
fi

# Running the tests
echo "Running tests tagged with $TAGS"

if [ "$TEST_PLAN" = "" ]; then
    pipenv run python -m pytest -s --reruns $RETRY --reruns-delay 1 --gherkin-terminal-reporter --driver Chrome --driver-path $DRIVER_PATH --capability headless $HEADLESS --variables webdriver/capabilities_web_local.json --base-url "$BASE_URL" --disable-warnings --tags="$TAGS"
else
    pipenv run python -m pytest -s --reruns $RETRY --reruns-delay 1 --gherkin-terminal-reporter --driver Chrome --driver-path $DRIVER_PATH --capability headless $HEADLESS --variables webdriver/capabilities_web_local.json --base-url "$BASE_URL" --disable-warnings --tags="$TAGS" --pytest-testrail-export-test-results --pytest-testrail-test-plan-id="$TEST_PLAN"
fi
