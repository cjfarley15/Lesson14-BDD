# Created by Connor at 11/22/2020
Feature:  Retirement Age Calculator
   Calculates a users Retirement Age

  Scenario:  Test the Calculator for a Month Value Error
    Given The user enters "1961"
    When The user enters "0"
    Then The result should be Value Error



  Scenario: # Test the Calculator for incorrect format
    Given The user enters "1980"
    When The user enters "Hello"
    Then The result should be Error


  Scenario Outline: # Testing the Calculator for Retirement Age 67
    Given User enters “<Year>”
    When User enters "<Month>"
    Then result should be “<Age>”

    Examples: Inputs
    | Year | Month | Age|
    | 1960 | 03    | 67 |
    | 1990 | 05    | 67 |
    | 2010 | 07    | 67 |
    | 2020 | 10    | 67 |


  Scenario Outline: # Testing the Calculator for Retirement Age 66
    Given User enters “<Year>”
    When User enters “<Month>”
    Then result should be “<Age>”

    Examples: Inputs
    | Year | Month | Age |
    | 1943 | 01    | 66  |
    | 1948 | 07    | 66  |
    | 1950 | 02    | 66  |
    | 1954 | 09    | 66  |


  Scenario Outline: Testing the Calculator for Retirement Age 65
    Given User enters “<Year>”
    And User enters “<Month>”
    Then result should be “<Age>”

    Examples:
    | Year | Month | Age |
    | 1900 | 02    | 65  |
    | 1910 | 05    | 65  |
    | 1920 | 08    | 65  |
    | 1930 | 11    | 65  |
    | 1937 | 12    | 65  |
