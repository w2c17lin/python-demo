#-*- coding:utf-8 -*-
import datetime
import getopt
import logging
import logging.config
import sys

import config
from selenium import webdriver
from spider.ctrip import Ctrip
from spider.qunar import Qunar
from spider.tuniu import Tuniu
from utils.dao import MySQLDao

# 设置默认参数
headless = False
date = datetime.date.today() + datetime.timedelta(days=1)
str_time = date.strftime('%Y-%m-%d')
# air_line = config.AIR_LINE
air_line = config.AIR_LINE_DEV

# 获取参数列表
try:
    opts, args = getopt.getopt(sys.argv[1:], 't:h', ['time=', 'headless'])
except getopt.GetoptError:
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-t", "--time"):
        time = arg
    elif opt in ('-h', '--headless'):
        headless = True

# 初始化日志
logging.config.fileConfig('./res/logging.conf')

# 初始化数据库
dao = MySQLDao('./res/mysql.conf')

# 初始化浏览器
options = webdriver.FirefoxOptions()
if(headless):
    options.add_argument('--headless')
browser = webdriver.Firefox(
    executable_path='./res/geckodriver.exe', log_path='./logs/geckodriver.log', firefox_options=options)

# 初始化爬虫
qunar = Qunar(browser, dao)
ctrip = Ctrip(browser, dao)
tuniu = Tuniu(browser, dao)

# 开始爬取
qunar.crawling(air_line, str_time)
ctrip.crawling(air_line, str_time)
tuniu.crawling(air_line, str_time)

# 结束
dao.close()
if(headless):
    browser.close()
