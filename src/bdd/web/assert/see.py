# -*- coding:utf-8 -*-

from lettuce import step, world


@step("I see current url is \'([^\']*)\'")
def i_see_current_url_is(_step, url):
    assert world.browser.current_url == url


@step("I see \'([^\']*)\' in the title")
def i_see_text_in_the_title(_step, text):
    assert text in world.browser.title


@step("I see \'([^\']*)\' in the body")
def i_see_text_in_body(_step, text):
    body = world.browser.find_element_by_tag_name('body')
    assert text in body.text


@step("I see \'([^\']*)\' in the element with id \'([^\']*)\'")
def i_see_text_in_the_element_with_id(_step, text, id):
    element = world.browser.find_element_by_id(id)
    element_text = element.get_attribute('value')
    assert text in element_text


@step("I see \'([^\']*)\' in the element with xpath \'([^\']*)\'")
def i_see_text_in_the_element_with_xpath(_step, text, xpath):
    element = world.browser.find_element_by_xpath(xpath)
    element_text = element.get_attribute('value')
    assert text in element_text


@step("I see \'([^\']*)\' in the element with name \'([^\']*)\'")
def i_see_text_in_the_element_with_name(_step, text, name):
    element = world.browser.find_element_by_name(name)
    element_text = element.text
    assert text in element_text


@step("I see \'([^\']*)\' in the element with css selector \'([^\']*)\'")
def i_see_text_in_the_element_with_css_selector(_step, text, css_selector):
    elements = world.browser.find_elements_by_css_selector(css_selector)
    element_text = [element.text for element in elements]
    assert text in element_text


@step("I see \'([^\']*)\' in the element with class \'([^\']*)\'")
def i_see_text_in_the_element_with_class(_step, text, _class):
    element = world.browser.find_element_by_class_name(_class)
    element_text = element.text
    assert text in element_text
