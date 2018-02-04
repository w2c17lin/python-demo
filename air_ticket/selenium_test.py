#-*- coding:utf-8 -*-
from log import Log
from selenium import webdriver

log = Log('logs')

browser = webdriver.PhantomJS()
browser.get('http://www.baidu.com/')
title = browser.title
body = browser.find_element_by_xpath('/html/body').text
log.info(title)
log.info(body)
print(body)

browser.quit()
