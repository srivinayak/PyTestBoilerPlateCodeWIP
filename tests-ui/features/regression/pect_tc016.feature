
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc016
Feature: User navigates For Pfizer Clinical Trial and searches for a Trial
     Background:
         Given The browser resolution is '1367' per '768'

     Scenario: PECT-TC016-A: User navigates to Find a Pfizer Clinical Trial and searches a Trial
         Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
         When I click on 'PECT > accept cookie'
         Then I expect that element 'PECT > home page > logo' is displayed
         Then I expect that element 'PECT > home page > search box' is displayed
         When I set text 'covid 19' to field 'PECT > home page > search box'
         When I set text 'New York' to field 'PECT > home page > location box'
         When I click on 'PECT > home page > find a trial'
         Then The page url contains 'https://www.pfizerclinicaltrials.com/find-a-trial'

    Scenario: PECT-TC016-B: User accesses Pfizer Clinical Trial and searches a Trial
         Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
         When I click on 'PECT > accept cookie'
         Then I expect that element 'PECT > home page > logo' is displayed
         When I hover over 'PECT > home page > find a trial nav'
         Then I expect that element 'PECT > home page > find trail search flyout' is displayed
         When I set text 'covid 19' to field 'PECT > home page > find trail search flyout'
         When I set text 'New York' to field 'PECT > home page > find trail location flyout'
         When I click on 'PECT > home page > find trail button flyout'
         Then The page url contains 'https://www.pfizerclinicaltrials.com/find-a-trial/covid%2019'


  Scenario: PECT-TC016-C: User accesses Pfizer Clinical Trial and Trial Search Result content
         Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
         When I click on 'PECT > accept cookie'
         Then I expect that element 'PECT > home page > logo' is displayed
         Then I expect that element 'PECT > home page > search box' is displayed
         When I set text 'covid 19' to field 'PECT > home page > search box'
         When I set text 'New York' to field 'PECT > home page > location box'
         When I click on 'PECT > home page > find a trial'
         Then The page url contains 'https://www.pfizerclinicaltrials.com/find-a-trial'
         Then I expect that element 'PECT > find a trail filter page > first search result' is displayed
         When I click on 'PECT > find a trail filter page > first search result'
         Then The page url contains 'https://www.pfizerclinicaltrials.com/find-a-trial'


