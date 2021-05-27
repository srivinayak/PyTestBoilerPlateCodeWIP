import base64
from io import BytesIO
from time import sleep

import cv2
import numpy
import logging
from PIL import Image

from pytest_selenium_enhancer import add_method
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger(__name__)


def my_custom_commands():

    @add_method(WebElement)
    def get_cropped_screenshot_as_base64(self, y_point=0):
        base_score = 0.94
        # Scroll element into view
        logger.info("About to get the screenshot cropped")
        self.parent.execute_script("window.scrollBy(0,100000)")
        sleep(1)
        actions = ActionChains(self.parent)
        self.parent.execute_script("arguments[0].scrollIntoView(true);", self)
        sleep(1)
        image_base_64 = self.parent.get_screenshot_as_base64()
        # im = Image.open(screenshot_url)
        im = Image.open(BytesIO(base64.b64decode(image_base_64)))
        im = im.crop((0, y_point, im.width, (im.height * 0.75 - y_point)))
        logger.info("Image cropping completed")
        return cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)

    # Does not work on mobile where location and size are not correctly calculated
    @add_method(WebElement)
    def get_screenshot_as_base64(self, threshold=0):
        logger.info("Started getting screenshot as base64")
        location = self.location
        size = self.size

        if self.parent.desired_capabilities['browserName'] in ["Chrome", "chrome", "MicrosoftEdge", "microsoftedge"]:
            self.parent.execute_script("window.scrollBy(0,100000)")
            sleep(1)
            # Scroll element into view
            actions = ActionChains(self.parent)
            actions.move_to_element(self).perform()
            sleep(1)
            location = self.location_once_scrolled_into_view

        if self.parent.desired_capabilities['browserName'] in ["Safari", "safari"]:
            self.parent.execute_script("window.scrollBy(0,100000)")
            sleep(1)
            # Scroll element into view
            self.parent.execute_script("arguments[0].scrollIntoView(true);", self)
            sleep(1)
            location = self.location_once_scrolled_into_view

        x_point = location['x']
        width = location['x'] + size['width']

        # Is needed for iOS screenshot to remove browser header controls.
        # On iOS the screenshot includes browser header and footer controls
        y_point = location['y'] + threshold
        height = location['y'] + size['height'] - threshold

        logger.debug("Calling WebElement class get screenshot method ")
        image_base_64 = self.parent.get_screenshot_as_base64()
        # im = Image.open(screenshot_url)
        img = Image.open(BytesIO(base64.b64decode(image_base_64)))
        img = img.crop((int(x_point), int(y_point), int(width), int(height)))
        logger.info("Get screenshot as Base64 completed")
        return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

    @add_method(WebElement)
    def is_in_viewport(self):
        logger.info("Verifying if element is in view port")
        script = 'if (!arguments[0].getBoundingClientRect) { \n' \
                 '    return false \n' \
                 '}; \n' \
                 'const rect = arguments[0].getBoundingClientRect(); \n' \
                 'const windowHeight = (window.innerHeight || document.documentElement.clientHeight); \n' \
                 'const windowWidth = (window.innerWidth || document.documentElement.clientWidth); \n' \
                 'const vertInView = (rect.top <= windowHeight) && ((rect.top + rect.height) > 0); \n' \
                 'const horInView = (rect.left <= windowWidth) && ((rect.left + rect.width) > 0); \n' \
                 'return (vertInView && horInView);'
        is_in_view = self.parent.execute_script(script, self)
        logger.info("Is element present in view port: ", is_in_view)
        return is_in_view
