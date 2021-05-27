
#
# Author: ITTDigital
#
#Feature: User navigates For Current Clinical Trial Participants and verifies Download option presence
@automated @pect_test @pect_tc013
Feature: Default Section 1
    description 1
    Background:
        Given The browser resolution is '1367' per '768'

    @TR-C7 @automated
    Scenario: PECT-TC013-A: User accesses Clinical Trial Participants and verifies Download option
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        Then I expect that element 'PECT > home page > logo' is displayed
        When I hover over 'PECT > home page > for participants flyout'
        Then I expect that element 'PECT > home page > for current clinical trial participant' is displayed
        When I click on 'PECT > home page > for current clinical trial participant'
        Then The page url is 'https://www.pfizerclinicaltrials.com/for-current-clinical-trial-participants'
        Then I expect that element 'PECT > current clinical trail participants > current participant header' is displayed
        Then I expect that element 'PECT > current clinical trail participants > current participant banner' is displayed
        Then I expect that element 'PECT > current clinical trail participants > download checklist button' is displayed
