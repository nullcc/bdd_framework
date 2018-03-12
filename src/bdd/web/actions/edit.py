# -*- coding:utf-8 -*-

from lettuce import step, world
from selenium import webdriver


@step("I input \'([^\']*)\' in element with id \'([^\']*)\'")
def i_input_text_in_element_with_id(_step, text, id):
    element = world.browser.find_element_by_id(id)
    element.click()
    element.send_keys(text)

