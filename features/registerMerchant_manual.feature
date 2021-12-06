
  Feature: Manual Merchant Registration

    @regression
    Scenario Outline: Verify that amount is collected when register merchant API is executed
      Given user basic information is provided
      When user executed API with <amount>
      Then status code is returned
      Examples:
        |amount  |
        | 10     |

