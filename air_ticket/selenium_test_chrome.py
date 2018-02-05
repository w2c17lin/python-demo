#-*- coding:utf-8 -*-
from log import Log
from selenium import webdriver

log = Log('logs')

options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
browser.get('http://www.baidu.com/')
title = browser.title
body = browser.find_element_by_xpath('/html/body').text
log.info(title)
log.info(body)

browser.quit()
