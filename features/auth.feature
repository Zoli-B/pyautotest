Feature: Login in page
  As a tester
  I want to login with username and password


Scenario: Login
  Given a főoldalon vagyok
  When ráklikkelek a "auth" kulcsú elemre
  Then az URL "/basic_auth" végződésre vált
  When beírtam a felhasználónevet és a jelszót
  Then Congratulations! You must have the proper credentials. szöveget kapom vissza