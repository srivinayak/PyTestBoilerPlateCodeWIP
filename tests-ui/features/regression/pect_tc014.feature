
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc014
Feature: User navigates a Landing Page End and Performs Go Back To Top
    Background:
        Given The browser resolution is '1367' per '768'

  Scenario: PECT-TC014-A: User accesses Clinical Trial Participants and performs go back to top
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I click on 'PECT > accept cookie'
      When I hover over 'PECT > home page > for participants flyout'
      Then I expect that element 'PECT > home page > for current clinical trial participant' is displayed
      When I click on 'PECT > home page > for current clinical trial participant'
      Then The page url is 'https://www.pfizerclinicaltrials.com/for-current-clinical-trial-participants'
      Then I expect that element 'PECT > current clinical trail participants > current participant header' is displayed
#### Need to add the custom steps for scrolling down to the bottom and top of the page
#      Then PECT_TC014_A User then scrolls down the utmost last of the Landing Page
#      Then PECT_TC014_A User then tries use Go Back To Top option

  Scenario: PECT-TC014-B: User accesses FAQs and performs go back to top
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      When I click on 'PECT > accept cookie'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I hover over 'PECT > home page > about clinical trials drop down'
      Then I expect that element 'PECT > home page > clinical trials FAQ' is displayed
      When I click on 'PECT > home page > clinical trials FAQ'
      Then The page url is 'https://www.pfizerclinicaltrials.com/about/frequently-asked-questions'
#### Need to add the custom steps for scrolling down to the bottom and top of the page
#      Then PECT_TC014_B User then scrolls down the utmost last of the Landing Page
#      Then PECT_TC014_B User then tries use Go Back To Top option

