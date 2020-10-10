Feature: Crypto.com Exchange

    Scenario: Accessing trade page about CRO/USDC
        Given I am on exchange page
        When I click "CRO Markets" tab
        And I click "CRO/USDC" item
        Then I should be on CRO/USDC trade page
