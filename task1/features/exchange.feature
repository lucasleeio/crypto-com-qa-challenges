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
            | 5   | sell     |
            | -1  | buy      |
            | -5  | buy      |

    Scenario Outline: Calculating total in trade form
        Given I am on CRO/USDC trade page
        When I input "<price>" into price of "<buy/sell>" trade form
        And  I input "<amount>" into amount of "<buy/sell>" trade form
        Then I should see "<total>" calculated in "<buy/sell>" trade form

        Examples:
            | buy/sell | price  | amount      | total         |
            | buy      | 0.1600 | 4           | 0.640000      |
            | buy      | 0.2020 | 4.594       | 0.927988      |
            | buy      | 0.1569 | 1126689.883 | 176777.642643 |
            | sell     | 0.1600 | 4           | 0.640000      |
            | sell     | 0.1020 | 56.984      | 5.812368      |
            | sell     | 0.1533 | 1335450.806 | 204724.608560 |
