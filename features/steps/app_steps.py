# features/steps/app_steps.py
from behave import given, when, then
from drivers.android_driver import AndroidDriver
from drivers.ios_driver import IOSDriver

@given('I have an Android device')
def step_impl(context):
    context.driver = AndroidDriver().get_driver()

@when('I launch the Android app')
def step_impl(context):
    context.driver.launch_app()

@then('the app should launch successfully')
def step_impl(context):
    assert context.driver.is_app_installed("com.example.androidapp")

@given('I have an iOS device')
def step_impl(context):
    context.driver = IOSDriver().get_driver()

@when('I launch the iOS app')
def step_impl(context):
    context.driver.launch_app()

@then('the app should launch successfully')
def step_impl(context):
    assert context.driver.is_app_installed("com.example.iosapp")
