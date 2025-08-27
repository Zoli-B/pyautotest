Feature: Disappearing Elements
  As a tester
  I want to try click the Disappearing Elements



  Scenario: Disappearing Elements Test
    Given a főoldalon vagyok
    When ráklikkelek a "dis_element" kulcsú elemre
    Then az URL "/disappearing_elements" végződésre vált
    When ráklikkelek a "dis_home" kulcsú elemre
    Then Megvizsgálom, hogy a főoldalon vagyok-e
    When ráklikkelek a "dis_element" kulcsú elemre
    When ráklikkelek a "dis_about" kulcsú elemre
    Then az URL "/about/" végződésre vált
    When visszalépek az előző oldalra
    When ráklikkelek a "dis_contect" kulcsú elemre
    Then az URL "/contact-us/" végződésre vált
    When visszalépek az előző oldalra
    When ráklikkelek a "dis_portfolio" kulcsú elemre
    Then az URL "/portfolio/" végződésre vált
    When visszalépek az előző oldalra
    When megkeresem az eltűnt elemet és rákattintok
    Then az URL "/gallery/" végződésre vált