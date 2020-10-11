Feature: Crypto.com Exchange

    Scenario: Accessing trade page about CRO/USDC
        Given I am on exchange page
        When I click "CRO Markets" tab
        And I click "CRO/USDC" item
        Then I should be on CRO/USDC trade page

    Scenario Outline: Putting price and sum from depth table into trade form
        Given I am on CRO/USDC trade page
        When I click row "<row>" in depth table
        Then I should see its price and sum put into "<buy/sell>" trade form

        Examples:
            | row | buy/sell |
            | 1   | sell     |
            | 2   | sell     |
            | -1  | buy      |
            | -2  | buy      |