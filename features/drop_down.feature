Feature: DropDown
  As a tester
  I want to try test DropDown List




  Scenario: Drop Down Test
    Given a főoldalon vagyok
    When ráklikkelek a "drop_down" kulcsú elemre
    Then az URL "/dropdown" végződésre vált
    When Kiválasztom "drop_down_menu" kulcsú elemet
    When Kiválasztom "drop_down_1" kulcsú elemet
    Then Megvizsgálom a változást
    When Kiválasztom a "drop_down_2" kulcsú elemet
    Then Megvizsgálom a változást