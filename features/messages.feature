Feature: Messages

Background: User Logs in
    Given User is on login page
    When User enters valid username
    And User enters valid password
    And User click on login button

Scenario: Verify user can send a message to admin
    When User clicks on Messages icon
    And User clicks on new message button
    And User enters message subject
    And User enters message body
    And User clicks send message
    Then "message has been sent" text is displayed