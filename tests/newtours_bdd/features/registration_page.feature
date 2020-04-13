Feature: User operates in registration page
  which is available at: http://newtours.demoaut.com/mercuryregister.php

  Background: Go to main newtours page
    Given page http://newtours.demoaut.com/mercuryregister.php is displayed

  Scenario: User wants to registry
    When user insert register credentials
    And user clicks register
    Then user should be moved to another site
    And verify is message "Dear Jan Kowalski" exists on page
    And verify is message "Thank you for registering." exists on page
