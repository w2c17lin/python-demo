#-*- coding:utf-8 -*-
import logging
from .util import repalce_url

# 去哪儿网址
QUNAER_URL = 'https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=#{from}&searchArrivalAirport=#{to}&searchDepartureTime=#{time}'


class Qunaer():
    def __init__(self, browser, dao):
        """
        构造函数

        @param browser 用于爬虫的浏览器
        @param log 日志工具
        """
        self.__log = logging.getLogger('app.qunaer')
        self.__brower = browser
        self.__dao = dao

    def crawling(self, air_line, time):
        """
        开始爬取

        @param air_line 要爬取的航班路线
        @param time 要爬取的航班时间
        """
        for value in air_line:
            url = repalce_url(QUNAER_URL, value['from'], value['to'], time)
            self.__log.debug('获取去哪儿机票信息 from %s to %s time %s',
                             value['from'], value['to'], time)
            self.__chrome(url)

    def __chrome(self, url):
        """
        开始获取数据

        @param url 已经构造好的网页地址
        """
        self.__browser.get(url)
