#-*- coding:utf-8 -*-
import logging
import logging.config

import config
from chrome.qunaer import Qunaer
from selenium import webdriver
from utils.dao import MySQLDao

# 初始化日志
logging.config.fileConfig('./res/logging.conf')

# 初始化数据库
dao = MySQLDao('./res/mysql.conf')

# 初始化浏览器
options = webdriver.ChromeOptions()
# options.add_argument('headless')
browser = webdriver.Chrome('./res/chromedriver.exe', chrome_options=options)

qunaer = Qunaer(browser, dao)
qunaer.crawling(config.AIR_LINE, '2017-01-23')

# browser.close()
