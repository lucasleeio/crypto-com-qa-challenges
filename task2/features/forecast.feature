Feature: MyObservatory 9-day forecast

    Scenario: Testing the 9-day forecast API
        When I send a request using the API
        Then the API should response success
        And I extract the relative humidity for the day after tomorrow
