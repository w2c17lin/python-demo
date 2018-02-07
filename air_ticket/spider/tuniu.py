#-*- coding:utf-8 -*-
import logging
import time
from datetime import datetime

from .util import random_num, repalce_url

# 途牛网址
TUNIU_URL = 'http://flights.ctrip.com/booking/#{from}-#{to}-day-1.html?DDate1=#{time}'
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
        url = repalce_url(TUNIU_URL, 'CKG', 'BJS', '2018-02-11')
        self.__log.debug('获取途牛机票信息 from %s to %s time %s' %
                         ('CKG', 'BJS', '2018-02-11'))
        self.__chrome(url)
        # for value in air_line:
        #     url = repalce_url(QUNAR_URL, value['from_code'], value['to_code'], time)
        #     self.__log.debug('获取途牛机票信息 from %s to %s time %s',
        #                      value['from'], value['to'], time)
        #     self.__chrome(url)

    def __chrome(self, url):
        """
        开始获取数据

        @param url 已经构造好的网页地址
        """
        self.__log.debug('打开网页信息...')
        self.__browser.implicitly_wait(10)
        self.__browser.get(url)

        index_list = self.__index_list()
        self.__log.debug('随机抓取10条机票信息: %s' % (index_list))

        airline_element = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]//td[@class="logo"]//strong')  # 航空公司信息
        flight_code_element = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]//td[@class="logo"]//div[@class="clearfix J_flight_no"]')  # 航班信息,飞机编号
        flight_name_element = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]//td[@class="logo"]//span[contains(@class, "direction_black_border craft J_craft")]')  # 航班信息,飞机名字
        depart_time_element = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]//td[@class="right"]//strong')  # 出发时间
        arrive_time_element = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]//td[@class="left"]//strong')  # 到达时间
        depart_airport_element = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]//td[@class="right"]//div')  # 出发机场
        arrive_airport_element = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]//td[@class="left"]//div')  # 到达机场
        price_element = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]//td[contains(@class, "price ")]//span[@class="base_price02"]')  # 机票价格

        for index in index_list:
            e = index * 2 + 1
            air = {
                'source': TUNIU_SOURCE,
                'spider_time': datetime.now(),
                'airline': airline_element[index].text,
                'flight': flight_code_element[index].get_attribute('data-flight') + ' ' + flight_name_element[index].text,
                'depart_time': depart_time_element[index].text,
                'arrive_time': arrive_time_element[index].text,
                'space_time': '',
                'depart_airport': depart_airport_element[e].text,
                'arrive_airport': arrive_airport_element[e].text,
                'price': int(price_element[index].text.replace('¥', ''))
            }
            self.__dao.insert(air)  # 插入数据库

    def __index_list(self):
        s_num = 0
        e_num = 1
        self.__log.debug('加载所有航班信息...')
        while e_num > s_num:
            elements = self.__browser.find_elements_by_xpath(
                '//div[@class="search_box search_box_tag search_box_light "]')
            s_num = len(elements)

            elements[s_num - 1].location_once_scrolled_into_view  # 滑动加载所有数据
            time.sleep(1)  # 延时1秒后再次获取数据

            elements = self.__browser.find_elements_by_xpath(
                '//div[@class="search_box search_box_tag search_box_light "]')
            e_num = len(elements)
            self.__log.debug('滑动页面到底部,s_num %d, e_num %d' % (s_num, e_num))
        return random_num(e_num)
