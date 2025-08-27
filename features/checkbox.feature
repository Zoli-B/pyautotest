Feature: CheckBox
  As a tester
  I want to try checkboxes



  Scenario: CheckBox Test
    Given a főoldalon vagyok
    When ráklikkelek a "check_box" kulcsú elemre
    Then az URL "/checkboxes" végződésre vált
    When rákattintok a "cb1" boxra
    Then megvizsgálom a változást
    When rákattintok a "cb2" boxra
    Then megvizsgálom a változást