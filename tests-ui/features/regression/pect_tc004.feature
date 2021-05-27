
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc004
Feature: User navigates to Home Page and accesses 'Learn more about your rights as a participant' link
    Background:
        Given The browser resolution is '1367' per '768'

    Scenario: PECT-TC004-A: Accesses Participant Rights Link
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        When I click on 'PECT > home page > learn more as participant'
        Then The page url is 'https://www.pfizerclinicaltrials.com/about/protecting-your-safety-and-privacy'
        Then I expect that element 'PECT > safety and privacy page > clinical trial safeguard video' is displayed
