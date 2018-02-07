#-*- coding:utf-8 -*-
import logging
import time
from datetime import datetime

from .util import random_num, repalce_url

# 去哪儿网址
QUNAR_URL = 'https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=#{from}&searchArrivalAirport=#{to}&searchDepartureTime=#{time}'
QUNAR_SOURCE = '去哪儿'


class Qunar():
    def __init__(self, browser, dao):
        """
        构造函数

        @param browser 用于爬虫的浏览器
        @param dao 数据库操作
        """
        self.__log = logging.getLogger('app.qunar')
        self.__browser = browser
        self.__dao = dao

    def crawling(self, air_line, time):
        """
        开始爬取

        @param air_line 要爬取的航班路线
        @param time 要爬取的航班时间
        """
        url = repalce_url(QUNAR_URL, '重庆', '北京', '2018-02-11')
        self.__log.debug('获取去哪儿机票信息 from %s to %s time %s' %
                         ('重庆', '北京', '2018-02-11'))
        self.__chrome(url)
        # for value in air_line:
        #     url = repalce_url(QUNAR_URL, value['from'], value['to'], time)
        #     self.__log.debug('获取去哪儿机票信息 from %s to %s time %s',
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
        for i in index_list:
            index = i % 20  # 计算要获取数据的index位置
            page_num = i // 20 + 1  # 计算要获取数据的页面编号
            self.__log.debug('当前页面 %d, 当前index %d' % (page_num, index))

            self.__goto_page(page_num)  # 跳转页面

            # 当前页面机票信息元素,用于点击详情获取机票价格
            elements = self.__browser.find_elements_by_xpath(
                '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]')
            self.__log.debug('点击详情,获取机票价格index %d' % (index))
            elements[0].location_once_scrolled_into_view
            elements[index].click()

            airline_element = self.__browser.find_elements_by_xpath(
                '//div[@class="col-airline"]//div[@class="air"]//span')  # 航空公司信息
            flight_element = self.__browser.find_elements_by_xpath(
                '//div[@class="col-airline"]//div[@class="num"]//span[@class="n"]')  # 航班信息
            depart_time_element = self.__browser.find_elements_by_xpath(
                '//div[@class="col-time"]//div[@class="sep-lf"]//h2')  # 出发时间
            arrive_time_element = self.__browser.find_elements_by_xpath(
                '//div[@class="col-time"]//div[@class="sep-rt"]//h2')  # 到达时间
            space_time_element = self.__browser.find_elements_by_xpath(
                '//div[@class="col-time"]//div[@class="sep-ct"]//div[@class="range"]')  # 花费时间
            depart_airport_element = self.__browser.find_elements_by_xpath(
                '//div[@class="col-time"]//div[@class="sep-lf"]//p[@class="airport"]//span')  # 出发机场
            arrive_airport_element = self.__browser.find_elements_by_xpath(
                '//div[@class="col-time"]//div[@class="sep-rt"]//p[@class="airport"]//span')  # 到达机场
            price_element = self.__browser.find_element_by_xpath(
                '//div[@class="clear-both"]//div[@class="prc lowprc"]//span')  # 机票价格

            s = index * 2
            e = s + 1
            air = {
                'source': QUNAR_SOURCE,
                'spider_time': datetime.now(),
                'airline': airline_element[index].text,
                'flight': flight_element[s].text + ' ' + flight_element[e].text,
                'depart_time': depart_time_element[index].text,
                'arrive_time': arrive_time_element[index].text,
                'space_time': space_time_element[index].text,
                'depart_airport': depart_airport_element[s].text + depart_airport_element[e].text,
                'arrive_airport': arrive_airport_element[s].text + arrive_airport_element[e].text,
                'price': int(price_element.text)
            }

            self.__log.debug('收起详情页index %d' % (index))
            elements[0].location_once_scrolled_into_view
            elements[index].click()
            self.__dao.insert(air)  # 插入数据库

    def __index_list(self):
        """
        获取当前路线全部数量,并生成该范围的十个随机数

        """
        self.__log.debug('获取当前路线总数据量....')
        page_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="m-page"]//a[@class="page"]')
        page_num = len(page_elements) + 1
        if page_num > 1:
            page_elements[len(page_elements) - 1].click()
        elements = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]')
        return random_num(len(elements), page_num)

    def __goto_page(self, page_num):
        """
        页面跳转

        @param page_num 要跳转的页面
        """
        page_elements = self.__browser.find_elements_by_xpath(
            '//div[@class="m-page"]//a[@class="page"]')
        for page_element in page_elements:
            if int(page_element.text) == page_num:
                self.__log.debug('跳转到页面 %d' % (page_num))
                page_element.click()
                return
