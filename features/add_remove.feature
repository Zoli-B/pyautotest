Feature: Add/Remove Elements
  As a tester
  I want to add and remove elements
  So that I can verify dynamic DOM changes

  Scenario: Add then delete an element
    Given a főoldalon vagyok
    When ráklikkelek a "add_remove_link" kulcsú elemre
    Then az URL "/add_remove_elements/" végződésre vált
    When ráklikkelek a "add_button" kulcsú elemre
    And megpróbálom törölni az elemet
    Then legalább 0 és legfeljebb 1 "delete_button" gomb látható
