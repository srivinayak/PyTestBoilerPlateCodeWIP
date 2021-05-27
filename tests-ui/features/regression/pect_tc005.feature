
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc005
Feature: User accesses About Pfizer Eclinical Trial Portal and accesses Other Diseases in the Vaccines Page

    Background:
        Given The browser resolution is '1367' per '768'

    Scenario: PECT-TC005-A: Accesses Other Diseases in Vaccines Page
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        Then I expect that element 'PECT > home page > logo' is displayed
        When I click on 'PECT > home page > our research'
        Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
        Then I expect that element 'PECT > our research page > vaccines' is displayed
        When I click on 'PECT > our research page > vaccines'
        Then The page url is 'https://www.pfizerclinicaltrials.com/our-research/vaccines'
        Then I expect that element 'PECT > vaccine clinical trials page > covid 19' is displayed
        Then I expect that element 'PECT > vaccine clinical trials page > respiratory' is displayed
        Then I expect that element 'PECT > vaccine clinical trials page > meningococcal' is displayed
        Then I expect that element 'PECT > vaccine clinical trials page > pneumococcal' is displayed
        When I click on 'PECT > vaccine clinical trials page > respiratory'
        Then The page url contains 'https://www.pfizerclinicaltrials.com/find-a-trial/RSV%20infection,Respiratory%20syncytial%20virus'
        Then I expect that element 'PECT > trials search result page > search result' is displayed
