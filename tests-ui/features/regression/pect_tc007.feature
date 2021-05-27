
#
# Author: ITTDigital
#
@automated @pect_test @pect_tc007
Feature: User navigates to 'Any' One of the pages and the tries to check the presence of a video
    Background:
        Given The browser resolution is '1367' per '768'

    Scenario: PECT-TC007-A: Confirm Presence of a Video in a Page
        Given I navigate to external page 'https://www.pfizerclinicaltrials.com/'
        Then I expect that element 'PECT > home page > logo' is displayed
        When I click on 'PECT > home page > our research'
        Then The page url is 'https://www.pfizerclinicaltrials.com/our-research'
        Then I expect that element 'PECT > our research page > text banner' is displayed
        Then I expect that element 'PECT > our research page > video' is displayed
