Feature: Find the Broken images



  Scenario: Broken Images
    Given a főoldalon vagyok
    When ráklikkelek a "broken_image" kulcsú elemre
    Then az URL "/broken_images" végződésre vált
    When Megvizsgálom vannak-e kép elemek az oldalon
    When Megvizsgálom melyik kép sérült
    Then 2 sérült képet találok

