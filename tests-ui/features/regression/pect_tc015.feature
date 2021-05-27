
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc015
Feature: User navigates For Current Clinical Trial Participants and checks URL route

  Scenario: PECT-TC015-A: User accesses Current Clinical Trial Participants and checks URL route
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      When I click on 'PECT > accept cookie'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I hover over 'PECT > home page > for participants flyout'
      Then I expect that element 'PECT > home page > for current clinical trial participant' is displayed
      When I click on 'PECT > home page > for current clinical trial participant'
      Then The page url is 'https://www.pfizerclinicaltrials.com/for-current-clinical-trial-participants'
      Then I expect that element 'PECT > current clinical trail participants > current participant header' is displayed

