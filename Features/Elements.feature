Feature: Test Suites Elements
  Scenario Outline: Elements
    Given I load the website
    When i go to "/text-box"
    Then I complete the text boxes
    Examples:
      |  |
