# -*- coding:utf-8 -*-

from lettuce import step, world
from selenium import webdriver


@step("I click element with id \'([^\']*)\'")
def i_click_element_with_id(_step, id):
    element = world.browser.find_element_by_id(id)
    element.click()


@step("I click element with class \'([^\']*)\'")
def i_click_element_with_class(_step, _class):
    element = world.browser.find_element_by_class_name(_class)
    element.click()


@step("I click element with link text \'([^\']*)\'")
def i_click_element_with_link_text(_step, text):
    element = world.browser.find_element_by_link_text(text)
    element.click()
