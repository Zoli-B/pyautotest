Feature: Drag And Drop
  As a tester
  I want to try Drop "A" to "B" and "B" to "A"



  Scenario: Drag And Drop Test
    Given a főoldalon vagyok
    When ráklikkelek a "dd" kulcsú elemre
    Then az URL "/drag_and_drop" végződésre vált
    When A "dd_a" elemet áthúzom a "dd_b" elemre
    Then Megvizsgálom, hogy helyet cseréltek-e
    When A "dd_b" elemet áthúzom a "dd_a" elemre
    Then Megvizsgálom, hogy helyet cseréltek-e ismét