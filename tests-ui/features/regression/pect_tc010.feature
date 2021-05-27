
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc010
Feature: User navigates to Our research and accesses Internal Medicine
    Background:
        Given The browser resolution is '1367' per '768'

  Scenario: PECT-TC010-A: User accesses Internal Medicine from Research page
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I click on 'PECT > home page > our research'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
      Then I expect that element 'PECT > our research page > text banner' is displayed
      When I click on 'PECT > our research page > internal medicine'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research/internal_medicine'
      Then I expect that element 'PECT > internal medicine page > internal medicine header' is displayed
      Then I expect that element 'PECT > internal medicine page > internal medicine banner' is displayed

