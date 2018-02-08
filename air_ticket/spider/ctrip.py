#-*- coding:utf-8 -*-
import logging
import time
from datetime import datetime

from .util import random_num, repalce_url

# 携程网址
CTRIP_URL = 'http://flights.ctrip.com/booking/#{from}-#{to}-day-1.html?DDate1=#{time}'
CTRIP_SOURCE = '携程'


class Ctrip():
    def __init__(self, browser, dao):
        """
        构造函数

        @param browser 用于爬虫的浏览器
        @param dao 数据库操作
        """
        self.__log = logging.getLogger('app.ctrip')
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
                self.__log.debug('获取携程机票信息 from %s to %s time %s',
                                 value['from'], value['to'], time)
                value['time'] = time
                self.__chrome(value)
            except Exception as e:
                self.__log.debug('获取携程机票信息失败 from %s to %s time %s Exception: %s' % (
                    value['from'], value['to'], time, e))

    def __chrome(self, air_line):
        """
        开始获取数据

        @param url 已经构造好的网页地址
        """
        url = repalce_url(
            CTRIP_URL, air_line['from_code'], air_line['to_code'], air_line['time'])
        self.__log.debug('打开网页信息...')
        self.__browser.get(url)

        self.__scroll_page()
        elements = self.__browser.find_elements_by_xpath(
            '//div[@class="search_box search_box_tag search_box_light "]')
        index_list = random_num(len(elements))
        self.__log.debug('随机抓取10条机票信息: %s' % (index_list))

        for index in index_list:
            airline_element = elements[index].find_element_by_xpath(
                './/td[@class="logo"]//strong')  # 航空公司信息
            flight_code_element = elements[index].find_element_by_xpath(
                './/td[@class="logo"]//div[@class="clearfix J_flight_no"]')  # 航班信息,飞机编号
            flight_name_element = elements[index].find_element_by_xpath(
                './/td[@class="logo"]//span[contains(@class, "direction_black_border craft J_craft")]')  # 航班信息,飞机名字
            depart_time_element = elements[index].find_element_by_xpath(
                './/td[@class="right"]//strong')  # 出发时间
            arrive_time_element = elements[index].find_element_by_xpath(
                './/td[@class="left"]//strong')  # 到达时间
            depart_airport_element = elements[index].find_element_by_xpath(
                './/td[@class="right"]//div[last()]')  # 出发机场
            arrive_airport_element = elements[index].find_element_by_xpath(
                './/td[@class="left"]//div[last()]')  # 到达机场
            price_element = elements[index].find_element_by_xpath(
                './/td[contains(@class, "price ")]//span[@class="base_price02"]')  # 机票价格
            air = {
                'source': CTRIP_SOURCE,
                'time': air_line['time'],
                'depart': air_line['from'],
                'arrive': air_line['to'],
                'airline': airline_element.text,
                'flight': flight_code_element.get_attribute('data-flight') + ' ' + flight_name_element.text,
                'depart_time': depart_time_element.text,
                'arrive_time': arrive_time_element.text,
                'space_time': '',
                'depart_airport': depart_airport_element.text,
                'arrive_airport': arrive_airport_element.text,
                'price': int(price_element.text.replace('¥', ''))
            }
            self.__dao.insert(air)  # 插入数据库

    def __scroll_page(self):
        """
        由于携程是下滑加载元素,所以页面进入后开始模拟用户下滑操作,加载所有机票信息

        """
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
            self.__log.debug('滑动页面到底部, s_num %d, e_num %d' % (s_num, e_num))
