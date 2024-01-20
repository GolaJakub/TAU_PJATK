Feature: Amazon Adding to Cart

  Scenario: Add product to the cart on Amazon
    Given I open the Amazon website
    When I confirm the cookies
    When I search for the product "Iphone 13"
    And I click on the product
    And I click on the "Add to Cart" button
    Then the cart should contain 1 product
