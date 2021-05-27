
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc003
Feature: User accesses About PECT Portal and accesses COVID-19 in the Vaccines Page
    Background:
        Given The browser resolution is '1367' per '768'



    Scenario: PECT-TC003-A: Access COVID 19 information
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        Then I expect that element 'PECT > home page > logo' is displayed
        When I click on 'PECT > home page > covid-19 clinical trails'
        Then The page url is 'https://www.pfizerclinicaltrials.com/find-a-trial/COVID-19'
        Then I expect that element 'PECT > find a trail filter page > search box' is displayed



    Scenario: PECT-TC003-B: Validate certain COVID19 information
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        When I click on 'PECT > accept cookie'
        Then I expect that element 'PECT > home page > logo' is displayed
        When I click on 'PECT > home page > our research'
        Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
        Then I expect that element 'PECT > our research page > vaccines' is displayed
        When I click on 'PECT > our research page > vaccines'
        Then The page url is 'https://www.pfizerclinicaltrials.com/our-research/vaccines'
        When I click on 'PECT > vaccine clinical trials page > covid 19'
        Then The page url contains 'https://www.pfizerclinicaltrials.com/find-a-trial/Coronavirus%20,COVID-19'


  Scenario: PECT-TC003-C: Validate COVID 19 search data
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        When I click on 'PECT > accept cookie'
        When I search keywords 'Covid 19 | COVID 19' in field 'PECT > home page > search box' then I click 'PECT > home page > find a trial' and compare results count in 'PECT > find a trail filter page > search result count text'
        #When I search keywords 'Covid 19 | Acute HIV Infection' in field 'PECT > home page > search box' then I click 'PECT > home page > find a trial' and compare results count
        When I click on 'PECT > home page > find trail button flyout'
