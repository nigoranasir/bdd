# home.feature
Feature: Home Page

@smoke
Scenario: Verify bank-user can only access specific side menus
    Given user is logged in with bank-user role
    Then user can access "Accounts" side menu
    Then user can access "Cards" side menu
    Then user can access "Transfers" side menu
    Then user can access "Reports" side menu
    Then user can access "News" side menu
    Then user can access "My Profile" side menu
    Then user can not access "Requests" side menu
    Then user can not access "Profiles" side menu
    Then user can not access "System Log" side menu
    Then user can not access "Settings" side menu

@smoke
Scenario: Verify bank-admin can only access specific side menus
    Given user is logged in with bank-admin role
    Then user can access "Requests" side menu
    Then user can access "Accounts" side menu
    Then user can access "Profiles" side menu
    Then user can access "Transfers" side menu
    Then user can access "Messages" side menu
    Then user can access "News" side menu
    Then user can access "System Log" side menu
    Then user can access "Settings" side menu
    Then user can access "Reports" side menu
    Then user can not access "Cards" side menu
    Then user can not access "My Profile" side menu