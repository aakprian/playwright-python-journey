Feature: Order Flow
  As a registered user
  I want to place and verify my orders
  So that I can confirm my purchases are tracked correctly

  Scenario: Verify order confirmation message after login
    Given the user is on the login page
    When I login with valid credentials
    And I navigate to the orders page
    And I select the first order
    Then the order confirmation message is displayed