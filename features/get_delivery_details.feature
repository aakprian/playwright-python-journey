Feature: Get Delivery Details
  Tests to gets delivery details

  Scenario Outline: get delivery details of selected orderID
    Given
    And the user is on landing page
    When I login into portal with <username> and <password>
    And nagivate to orders page
    And select the order
    Then order msg is succesfully displayed
    Examples:
      | username             | password |
      |rahulshetty@gmail.com | Iamking@000|


