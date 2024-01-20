Feature: OrangeHRM Login and Add Employee

  Scenario: Automate login and adding employee
    Given I open the OrangeHRM website
    When I log in with username "Admin" and password "admin123"
    Then I should be successfully logged in
    When I add a new employee with details "Test", "Testowski", "Testowy":
    Then the employee should be successfully added
