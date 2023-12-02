Feature: Login Functionality

    As a user I would like to login and view my profile

@smoke
Scenario: Verfy user can login with valid credentials
    Given User is on login page
    When User enters valid username
    And User enters valid password
    And User click on login button
    Then "hello" text is displayed

Scenario Outline: Verify user will get error message invalid credentials are used
    Given User is on login page
    When User enters username "<username>"
    And User enters password "<password>"
    And User click on login button
    Then "<error>" text is displayed

    Examples:
        | username  | password      | error |
        | test111   | test222       | Wrong username or password    |
        | ab        | test          | Should be minimum 4 chars     |
        | blank         | test          | Field is required     |
        | test          | blank         | Field is required    