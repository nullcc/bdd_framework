Feature: baidu index page test case
  open browser, go to baidu index page, assert text, close browser

      Scenario: open baidu site
          Given I open web browser
          When I open page 'https://www.baidu.com/'
          Then I see current url is 'https://www.baidu.com/'
          Then I see '百度' in the title
          Then I see '关于百度' in the body
          Then I input 'Python' in element with id 'kw'
          Then I see 'Python' in the element with xpath '//*[@id="kw"]'
          Then I click element with class 's_btn'
          Then Sleep for '3' seconds
          Then I click element with link text '百度首页'
          Then I see '关于百度' in the body
          Then I see '学术' in the element with name 'tj_trxueshu'
          Then I see '新闻' in the element with css selector '.mnav'
          Then I see '新闻' in the element with class 'mnav'
          Then Get screen shot as file '../../../screenshots/baidu.png'
          Then I close web browser