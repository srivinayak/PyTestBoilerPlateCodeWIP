
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc009
Feature: User accesses About Pfizer Eclinical Trial Portal and accesses FAQs
    Background:
        Given The browser resolution is '1367' per '768'

  Scenario: PECT-TC009-A: Accesses FAQs in the Landing Page
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I hover over 'PECT > home page > about clinical trials drop down'
      Then I expect that element 'PECT > home page > clinical trials FAQ' is displayed
      When I click on 'PECT > home page > clinical trials FAQ'
      Then The page url is 'https://www.pfizerclinicaltrials.com/about/frequently-asked-questions'
      Then I expect that element 'PECT > frequently asked questions page > clinical trial banner' is displayed
      Then I expect that element 'PECT > frequently asked questions page > faq banner' is displayed


  Scenario: PECT-TC009-B: Accesses FAQs in the Landing Page
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I click on 'PECT > home page > about clinical trails resource'
      Then The page url is 'https://www.pfizerclinicaltrials.com/about-clinical-trials'
      Then I expect that element 'PECT > about clinical trail page > banner' is displayed
      Then I expect that element 'PECT > about clinical trail page > FAQs' is displayed
      When I click on 'PECT > about clinical trail page > see more'
      Then I expect that element 'PECT > about clinical trail page > learn more' is displayed
      When I click on 'PECT > about clinical trail page > learn more'
      Then The page url is 'https://www.pfizerclinicaltrials.com/about/frequently-asked-questions'


  Scenario: PECT-TC009-C: Searches FAQ in the Landing Page
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I hover over 'PECT > home page > about clinical trials drop down'
      Then I expect that element 'PECT > home page > clinical trials FAQ' is displayed
      When I click on 'PECT > home page > clinical trials FAQ'
      Then The page url is 'https://www.pfizerclinicaltrials.com/about/frequently-asked-questions'
      Then I expect that element 'PECT > frequently asked questions page > clinical trial banner' is displayed
      Then I expect that element 'PECT > frequently asked questions page > faq banner' is displayed
      ## Searching the FAQ
      #Then PECT_TC009_C User then searches the FAQ


  Scenario: PECT-TC009-D: Accesses FAQ and Expands the FAQ sections
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I hover over 'PECT > home page > about clinical trials drop down'
      Then I expect that element 'PECT > home page > clinical trials FAQ' is displayed
      When I click on 'PECT > home page > clinical trials FAQ'
      Then The page url is 'https://www.pfizerclinicaltrials.com/about/frequently-asked-questions'
      Then I expect that element 'PECT > frequently asked questions page > clinical trial banner' is displayed
      Then I expect that element 'PECT > frequently asked questions page > faq banner' is displayed
      When I click on 'PECT > frequently asked questions page > expand all'
      Then I expect that element 'PECT > frequently asked questions page > collapse all' is displayed
      Then I expect that element 'PECT > frequently asked questions page > learn more buttons' appears exactly '6' times
      Then I expect that element 'PECT > frequently asked questions page > is this helpful buttons' appears exactly '10' times


  Scenario: PECT-TC009-E: Accesses FAQ then Expands and Collapses the sections
      Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
      Then I expect that element 'PECT > home page > logo' is displayed
      When I hover over 'PECT > home page > about clinical trials drop down'
      Then I expect that element 'PECT > home page > clinical trials FAQ' is displayed
      When I click on 'PECT > home page > clinical trials FAQ'
      Then The page url is 'https://www.pfizerclinicaltrials.com/about/frequently-asked-questions'
      Then I expect that element 'PECT > frequently asked questions page > clinical trial banner' is displayed
      Then I expect that element 'PECT > frequently asked questions page > faq banner' is displayed
      When I click on 'PECT > frequently asked questions page > expand all'
      Then I expect that element 'PECT > frequently asked questions page > collapse all' is displayed
      When I click on 'PECT > frequently asked questions page > collapse all'
      Then I expect that element 'PECT > frequently asked questions page > expand all' is displayed
