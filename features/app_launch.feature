# features/app_launch.feature
Feature: Launch App

  Scenario: Launch Android App
    Given I have an Android device
    When I launch the Android app
    Then the app should launch successfully

  Scenario: Launch iOS App
    Given I have an iOS device
    When I launch the iOS app
    Then the app should launch successfully
