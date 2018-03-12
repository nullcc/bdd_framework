# -*- coding:utf-8 -*-

from lettuce import step, world
from selenium import webdriver


@step("I open web browser")
def i_open_web_browser(_step):
    world.browser = webdriver.Chrome()
    world.browser.maximize_window()


@step("I open page \'([^\']*)\'")
def i_open_page(_step, url):
    world.browser.get(url)


@step("I close web browser")
def i_close_web_browser(_step):
    world.browser.close()


@step("Sleep for \'([^\']*)\' seconds")
def sleep(_setp, seconds):
    seconds = int(seconds)
    import time
    time.sleep(seconds)


@step("Get screen shot as file \'([^\']*)\'")
def get_screen_shot_as_file(_step, filename):
    world.browser.get_screenshot_as_file(filename)
