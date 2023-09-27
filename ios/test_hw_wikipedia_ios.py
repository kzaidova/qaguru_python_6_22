from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from allure_commons._allure import step


def test_add_text_at_ui_elements():
    with step('Type email'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com' + '\n')

    with step('Verify added row'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('hello@browserstack.com'))

