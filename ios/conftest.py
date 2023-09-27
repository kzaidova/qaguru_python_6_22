from appium.options.ios import XCUITestOptions

import pytest

from appium import webdriver
from selene import browser
import os
import configuration
import attach

@pytest.fixture(scope='function', autouse=True)
def ios_mobile_management():
    options = XCUITestOptions().load_capabilities({

        "app": 'ios',

        "deviceName": configuration.settings.ios_device,
        "platformName": configuration.settings.ios_platform,
        "platformVersion": configuration.settings.ios_version,


        "bstack:options": {
            "userName": configuration.settings.browserstack_username,
            "accessKey": configuration.settings.browserstack_key,
            "projectName": configuration.settings.project_name,
            "buildName": configuration.settings.build_name,
            "sessionName": configuration.settings.session_name
    }
})

    browser.config.driver_remote_url = webdriver.Remote(configuration.settings.browserstack_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield
    attach.allure_attach_bstack_screenshot()
    browser.quit()
