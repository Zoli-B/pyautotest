Feature: Context Menu
  As a tester
  I want to try click the black box


  Scenario: Context Menu Test
    Given a főoldalon vagyok
    When ráklikkelek a "cm" kulcsú elemre
    Then az URL "/context_menu" végződésre vált
    When Jobb klikkel rákatintok a fekete elemre
    Then Megvizsgálom sikeres volt-e a kattintás