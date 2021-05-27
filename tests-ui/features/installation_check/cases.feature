@automated @installation_check @nondestructive
Feature: Check installation

    Scenario: Check project structure
        Then root folder structure is correct
        Then features folder structure is correct
        Then page_objects folder structure is correct
        Then screenshots folder structure is correct
        Then scripts folder structure is correct
        Then step_definitions folder structure is correct
        Then test_data folder structure is correct
        Then utils folder structure is correct
        Then webdriver folder structure is correct

    Scenario: Check browser configuration
        Given I navigate to external page 'https://www.google.com'
        Then The page url is 'https://www.google.com/'
