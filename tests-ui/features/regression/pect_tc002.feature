
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc002
Feature: User accesses the Pfizer Eclinical Trial Portal and accesses the TRIAL section
    Background:
        Given The browser resolution is '1367' per '768'
        #Given I am on the url 'https://www.pfizerclinicaltrials.com/'


    Scenario: PECT-TC002-A: Verification of certain TRIAL page contents
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        Then I expect that element 'PECT > home page > logo' is displayed
        When I click on 'PECT > home page > about clinical trials drop down'
        Then The page url is 'https://www.pfizerclinicaltrials.com/about-clinical-trials'
        Then I expect that the title is 'What are Clinical Trials? Facts About Research Studies | Pfizer'
        Then The element 'PECT > about clinical trail page > banner' text is 'Tomorrow’s breakthroughs start today…'


    Scenario: PECT-TC002-B: Access the Trial Filters
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        Then I expect that element 'PECT > home page > logo' is displayed
        When I click on 'PECT > home page > find a trial'
        Then The page url contains 'https://www.pfizerclinicaltrials.com/find-a-trial'
        When I set text 'Covid-19' to field 'PECT > find a trail filter page > search box'
        When I click on 'PECT > find a trail filter page > find button'
