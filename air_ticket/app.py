#-*- coding:utf-8 -*-
import logging
import logging.config

import config
from chrome.qunaer import Qunaer
from selenium import webdriver
from utils.dao import MySQLDao

logging.config.fileConfig('./res/logging.conf')

dao = MySQLDao()
# options = webdriver.ChromeOptions()
# options.add_argument('headless')

# browser = webdriver.Chrome('./res/chromedriver.exe', chrome_options=options)

# qunaer = Qunaer(browser, log)
# qunaer.crawling(config.AIR_LINE, '2017-01-23')

# browser.close()
