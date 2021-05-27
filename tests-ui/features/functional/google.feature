@automated @google
Feature: User searches keywords in google
    Background:
        Given The browser resolution is '1367' per '768'

    Scenario Outline: searches the keyword in google
        Given I navigate to external page 'https://www.google.co.in/'
        Then I expect that element 'google > search box' is displayed
        #When I enter text <keywords> to field 'google > search box'
        When I enter text <keywords>
        When I click on 'google > search button'


        Examples:
            | keywords |
            | hello    |
            | world    |
            | Kitty    |
