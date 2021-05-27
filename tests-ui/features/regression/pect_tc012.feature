
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc012
Feature: User navigates to Internal Medicine Page and accesses Email and Print Option
    Background:
        Given The browser resolution is '1367' per '768'

  Scenario: PECT-TC012-A: User accesses Internal Medicine and checks Email option
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I click on 'PECT > accept cookie'
      When I click on 'PECT > home page > our research'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
      Then I expect that element 'PECT > our research page > text banner' is displayed
      When I click on 'PECT > our research page > internal medicine'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research/internal_medicine'
      Then I expect that element 'PECT > internal medicine page > internal medicine header' is displayed
      Then I expect that element 'PECT > internal medicine page > internal medicine banner' is displayed
      Then I expect that element 'PECT > internal medicine page > share email icon' is displayed


  Scenario: PECT-TC012-B: User accesses Internal Medicine and checks Print option
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      When I click on 'PECT > accept cookie'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I click on 'PECT > home page > our research'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
      Then I expect that element 'PECT > our research page > text banner' is displayed
      When I click on 'PECT > our research page > internal medicine'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research/internal_medicine'
      Then I expect that element 'PECT > internal medicine page > internal medicine header' is displayed
      Then I expect that element 'PECT > internal medicine page > internal medicine banner' is displayed
      Then I expect that element 'PECT > internal medicine page > print icon' is displayed
