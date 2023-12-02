Feature: Accounts

# Background is like shared steps in Azure DevOps
Background: User Login
    Given User is on login page
    When User enters valid username
    And User enters valid password
    And User click on login button

Scenario: Verify user can view transaction details
    When User clicks on Accounts side menu
    And User randomly click on any transaction
    Then Transaction details displayed

Scenario: Verify user can change selected account from checking to savings
    When User clicks on Accounts side menu
    And User clicks on account number dropdown
    And User clicks on any savings account option 
    Then Savings account details are displayed

Scenario: Verify user can export transaction list into csv file
    When User clicks on Accounts side menu
    And User clicks on export icon
    Then list of transactions are exported as csv file