#-*- coding:utf-8 -*-
import datetime
import logging
import logging.config
import time

import config
from selenium import webdriver
from spider.ctrip import Ctrip
from spider.qunar import Qunar
from spider.tuniu import Tuniu
from utils.dao import MySQLDao

# 初始化日志
logging.config.fileConfig('./res/logging.conf')
log = logging.getLogger('app.main')

# 初始化数据库
log.debug('初始化数据库...')
dao = MySQLDao('./res/mysql.conf')

# 初始化浏览器
log.debug('初始化浏览器...')
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
browser = webdriver.Firefox(
    executable_path='./res/geckodriver.exe', log_path='./logs/geckodriver.log', firefox_options=options)

# 初始化爬虫
log.debug('初始化爬虫...')
qunar = Qunar(browser, dao)
ctrip = Ctrip(browser, dao)
tuniu = Tuniu(browser, dao)

# 开始爬取
spider_time = 1
while True:
    start_time = time.clock()
    date = datetime.date.today() + datetime.timedelta(days=1)
    str_time = date.strftime('%Y-%m-%d')

    log.debug('开始爬取数据 time %s' % (str_time))
    qunar.crawling(config.AIR_LINE, str_time)
    ctrip.crawling(config.AIR_LINE, str_time)
    tuniu.crawling(config.AIR_LINE, str_time)

    space_time = time.clock() - start_time
    log.debug('第%d轮爬取数据完成, 耗时 %ds, 休眠时间 %ds' %
              (spider_time, space_time, config.INTERVAL_TIME))
    spider_time += 1
    time.sleep(config.INTERVAL_TIME)

# 结束
dao.close()
browser.close()
