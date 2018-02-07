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
                url = repalce_url(
                    TUNIU_URL, value['from_code'], value['to_code'], time)
                self.__chrome(url)
                return
            except Exception as e:
                self.__log.debug('获取途牛机票信息失败 from %s to %s time %s Exception: \n%s' % (
                    value['from'], value['to'], time, e))

    def __chrome(self, url):
        """
        开始获取数据

        @param url 已经构造好的网页地址
        """
        self.__log.debug('打开网页信息...')
        self.__browser.implicitly_wait(10)
        self.__browser.get(url)

        elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]')

        i =0 
        for e in elements:
            print(elements[i].find_element_by_xpath(
                './/div[@class="fl-logo"]//div[@class="aircom"]').text)
            i = i+1
        return
        index_list = random_num(len(elements))
        self.__log.debug('随机抓取10条机票信息: %s' % (index_list))

        airline_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]//div[@class="fl-logo"]//div[@class="aircom"]')  # 航空公司信息
        flight_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]//div[@class="fl-logo"]//div[@class="flihtnumber left"]')  # 航班信息
        depart_time_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]//div[@class="fl-depart"]//p[@class="hours"]')  # 出发时间
        arrive_time_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]//div[@class="fl-arrive"]//span[@class="hours"]/span')  # 到达时间
        space_time_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]//div[@class="fl-center"]//p[@class="durationTime"]')  # 花费时间
        depart_airport_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]//div[@class="fl-depart"]//p[@class="airport"]')  # 出发机场
        arrive_airport_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]//div[@class="fl-arrive"]//p[@class="airport"]')  # 到达机场
        price_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="J-flightlist"]//div[@class="price"]//span[@class="num"]')  # 机票价格

        print('airline_elements %d' % (len(airline_elements)))
        print('flight_elements %d' % (len(flight_elements)))
        print('depart_time_elements %d' % (len(depart_time_elements)))
        print('arrive_time_elements %d' % (len(arrive_time_elements)))
        print('space_time_elements %d' % (len(space_time_elements)))
        print('depart_airport_elements %d' % (len(depart_airport_elements)))
        print('arrive_airport_elements %d' % (len(arrive_airport_elements)))
        print('price_elements %d' % (len(price_elements)))

        for index in index_list:
            s = index * 2
            e = s + 1
            air = {
                'source': TUNIU_SOURCE,
                'spider_time': datetime.now(),
                'airline': airline_elements[index].text,
                'flight': flight_elements[index].text,
                'depart_time': depart_time_elements[index].text,
                'arrive_time': arrive_time_elements[index].text,
                'space_time': space_time_elements[index].text,
                'depart_airport': depart_airport_elements[index].text,
                'arrive_airport': arrive_airport_elements[index].text,
                'price': int(price_elements[index].text)
            }
            self.__dao.insert(air)  # 插入数据库
