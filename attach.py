import allure
from selene import browser


def attach_browserstack_screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )
