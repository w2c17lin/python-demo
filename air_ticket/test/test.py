#-*- coding:utf-8 -*-
# import config
from selenium import webdriver
import logging
import logging.config
import configparser

cf = configparser.ConfigParser()
cf.read('./mysql.conf')
if cf.has_option('db', 'url'):
    print(cf.get('db', 'url'))
else: 
    print('dsf')

# logging.config.fileConfig('logging.conf')
# root_logger = logging.getLogger('main')
# root_logger.debug('test root logger...')


options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
browser.get('http://www.baidu.com/')
title = browser.title
body = browser.find_element_by_xpath('/html/body').text
print(title)
print(body)

# browser.quit()
