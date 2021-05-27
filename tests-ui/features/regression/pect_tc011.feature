
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc011
Feature: User navigates to Internal Medicine Page and accesses Like and Dislike button
    Background:
        Given The browser resolution is '1367' per '768'

  Scenario: PECT-TC011-A: User accesses Internal Medicine and clicks thumbs up
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I click on 'PECT > home page > our research'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
      Then I expect that element 'PECT > our research page > text banner' is displayed
      When I click on 'PECT > our research page > internal medicine'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research/internal_medicine'
      Then I expect that element 'PECT > internal medicine page > internal medicine header' is displayed
      Then I expect that element 'PECT > internal medicine page > internal medicine banner' is displayed
      When I click on 'PECT > internal medicine page > like page button'



  Scenario: PECT-TC011-B: User accesses Internal Medicine and checks thumbs down
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I click on 'PECT > home page > our research'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
      Then I expect that element 'PECT > our research page > text banner' is displayed
      When I click on 'PECT > our research page > internal medicine'
      Then The page url is 'https://www.pfizerclinicaltrials.com/our-research/internal_medicine'
      Then I expect that element 'PECT > internal medicine page > internal medicine header' is displayed
      Then I expect that element 'PECT > internal medicine page > internal medicine banner' is displayed
      When I click on 'PECT > internal medicine page > dislike page button'


