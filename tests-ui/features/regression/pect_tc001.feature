
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc001
Feature: User accesses the Pfizer Eclinical Trial Portal and verifies certain Home Page content
Background:
        Given The browser resolution is '1367' per '768'


  Scenario: PECT-TC001-A: Verification of Landing Page
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that the title is 'Pfizer Clinical Trials | Official Participant Site'
      Then I expect that element 'PECT > home page > logo' is displayed


  Scenario: PECT-TC001-B: Verification of certain Home Page contents
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > clinical trails image' is displayed
      Then I expect that element 'PECT > home page > current participants' is displayed
      Then I expect that element 'PECT > home page > clinical trails' appears exactly '4' times
