
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc006
Feature: User navigates to 'Our research' page using the 'Our research' link and verifies some Text Content
    Background:
        Given The browser resolution is '1367' per '768'


    Scenario: PECT-TC006-A: Verifies Text Content in the Research Page
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        Then I expect that element 'PECT > home page > logo' is displayed
        When I hover over 'PECT > home page > our research'
        Then I expect that element 'PECT > home page > visit our research page' is displayed
        When I click on 'PECT > home page > visit our research page'
        Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
        Then I expect that element 'PECT > our research page > text banner' is displayed

