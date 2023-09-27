import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
import configuration
import attach



@pytest.fixture(scope='function', autouse=True)
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({

        'platformName': configuration.settings.android_platform,
        'platformVersion': configuration.settings.android_version,
        'deviceName': configuration.settings.android_device,

        'app': configuration.settings.app_url,


        'bstack:options': {
            'projectName': configuration.settings.project_name,
            'buildName': configuration.settings.build_name,
            'sessionName': configuration.settings.session_name,

            'userName': configuration.settings.browserstack_username,
            'accessKey': configuration.settings.browserstack_key
        }
    })

    browser.config.driver_remote_url = configuration.settings.browserstack_url
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '20.0'))

    yield

    attach.attach_browserstack_screenshot()

    browser.quit()
