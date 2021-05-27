
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc008
Feature: User accesses the Pfizer Eclinical Trial Portal and Scrolls Down to Contact Us
    Background:
        Given The browser resolution is '1367' per '768'

    Scenario: PECT-TC008-A: Confirm Presence of Contact Us in a Page
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        Then I expect that element 'PECT > home page > logo' is displayed
        #Then Page scroll position is '768'
        Then I expect that element 'PECT > home page > contact us link' is displayed
        Then I expect that element 'PECT > home page > about us link' is displayed
        Then I expect that element 'PECT > home page > for investigators link' is displayed
