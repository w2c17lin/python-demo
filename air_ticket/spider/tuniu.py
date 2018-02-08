#-*- coding:utf-8 -*-
import logging
import time
from datetime import datetime

from .util import random_num, repalce_url

# 途牛网址
TUNIU_URL = 'http://flight.tuniu.com/domestic/list/#{from}_#{to}_ST_1_0_0/?start=#{time}'
TUNIU_SOURCE = '途牛'


class Tuniu():
    def __init__(self, browser, dao):
        """
        构造函数

        @param browser 用于爬虫的浏览器
        @param dao 数据库操作
        """
        self.__log = logging.getLogger('app.tuniu')
        self.__browser = browser
        self.__browser.implicitly_wait(10)
        self.__dao = dao

    def crawling(self, air_line, time):
        """
        开始爬取

        @param air_line 要爬取的航班路线
        @param time 要爬取的航班时间
        """
        for value in air_line:
            try:
                self.__log.debug('获取途牛机票信息 from %s to %s time %s',
                                 value['from'], value['to'], time)
                value['time'] = time
                self.__chrome(value)
            except Exception as e:
                self.__log.debug('获取途牛机票信息失败 from %s to %s time %s Exception: %s' % (
                    value['from'], value['to'], time, e))

    def __chrome(self, air_line):
        """
        开始获取数据

        @param url 已经构造好的网页地址
        """
        self.__log.debug('打开网页信息...')
        url = repalce_url(
            TUNIU_URL, air_line['from_code'], air_line['to_code'], air_line['time'])
        self.__browser.get(url)

        elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]')
        index_list = random_num(len(elements))
        self.__log.debug('随机抓取10条机票信息: %s' % (index_list))
        for index in index_list:
            airline_element = elements[index].find_element_by_xpath(
                './/div[@class="fl-logo"]//div[@class="aircom"]')  # 航空公司信息
            flight_element = elements[index].find_element_by_xpath(
                './/div[@class="fl-logo"]//div[@class="flihtnumber left"]')  # 航班信息
            depart_time_element = elements[index].find_element_by_xpath(
                './/div[@class="fl-depart"]//p[@class="hours"]')  # 出发时间
            arrive_time_element = elements[index].find_element_by_xpath(
                './/div[@class="fl-arrive"]//span[@class="hours"]/span')  # 到达时间
            space_time_element = elements[index].find_element_by_xpath(
                './/div[@class="fl-center"]//p[@class="durationTime"]')  # 花费时间
            depart_airport_element = elements[index].find_element_by_xpath(
                './/div[@class="fl-depart"]//p[@class="airport"]')  # 出发机场
            arrive_airport_element = elements[index].find_element_by_xpath(
                './/div[@class="fl-arrive"]//p[@class="airport"]')  # 到达机场
            price_element = elements[index].find_element_by_xpath(
                './/div[@class="price"]//span[@class="num"]')  # 机票价格
            air = {
                'source': TUNIU_SOURCE,
                'time': air_line['time'],
                'depart': air_line['from'],
                'arrive': air_line['to'],
                'airline': airline_element.text,
                'flight': flight_element.text,
                'depart_time': depart_time_element.text,
                'arrive_time': arrive_time_element.text,
                'space_time': space_time_element.text,
                'depart_airport': depart_airport_element.text,
                'arrive_airport': arrive_airport_element.text,
                'price': int(price_element.text)
            }
            self.__dao.insert(air)  # 插入数据库
