from appium.options.ios import XCUITestOptions

import pytest

from selene import browser
import os
import configuration
from utils import attach
from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def ios_mobile_management():
    options = XCUITestOptions().load_capabilities({

        "app": configuration.settings.ios_app_url,

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

    browser.config.driver = webdriver.Remote(configuration.settings.browserstack_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    yield
    attach.allure_attach_bstack_screenshot()
    browser.quit()
