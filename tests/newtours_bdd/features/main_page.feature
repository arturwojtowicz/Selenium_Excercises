Feature: User operates in main page
  which is available at: http://newtours.demoaut.com/

  Background: Go to main newtours page
    Given page http://newtours.demoaut.com/ is displayed

  Scenario: User log in
    When user insert login: "example.jan.kowalski@email.email" and password: "example_password"
    And user clicks sign-in
    Then user should be moved to another site

  Scenario: User wants to move to registration form by clicking "Register here"
    When user clicks "Register here" sign
    Then user should be moved to another site
