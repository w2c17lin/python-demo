#-*- coding:utf-8 -*-
import logging
import time
from .util import repalce_url

# 去哪儿网址
QUNAER_URL = 'https://flight.qunar.com/site/oneway_list.htm?' + \
    'searchDepartureAirport=#{from}&searchArrivalAirport=#{to}&searchDepartureTime=#{time}'


class Qunaer():
    def __init__(self, browser, dao):
        """
        构造函数

        @param browser 用于爬虫的浏览器
        @param log 日志工具
        """
        self.__log = logging.getLogger('app.qunaer')
        self.__browser = browser
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
                             '重庆', '北京', '2018-02-11')
            self.__chrome(url)
            return

    def __chrome(self, url):
        """
        开始获取数据

        @param url 已经构造好的网页地址
        """
        self.__browser.get(url)
        self.__browser.implicitly_wait(10)
        air = []
        # 当前页面机票信息元素
        elements = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]')
        # 航空公司信息
        airline_element = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]//div[@class="col-trip"]//div[@class="col-airline"]//div[@class="air"]//span[@class="n"]')
        # 航班信息
        flight_element = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]//div[@class="col-trip"]//div[@class="col-airline"]//div[@class="num"]//span[@class="n"]')
        # 出发时间
        depart_time_element = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]//div[@class="col-trip"]//div[@class="col-time"]//div[@class="sep-lf"]//h2')
        # 到达时间
        arrive_time_element = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]//div[@class="col-trip"]//div[@class="col-time"]//div[@class="sep-rt"]//h2')
        # 花费时间
        space_time_element = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]//div[@class="col-trip"]//div[@class="col-time"]//div[@class="sep-ct"]//div[@class="range"]')
        # 出发机场
        depart_airport_element = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]//div[@class="col-trip"]//div[@class="col-time"]//div[@class="sep-lf"]//p[@class="airport"]//span')
        # 到达机场
        arrive_airport_element = self.__browser.find_elements_by_xpath(
            '//div[@class="m-airfly-lst"]//div[@class="e-airfly"]//div[@class="col-trip"]//div[@class="col-time"]//div[@class="sep-rt"]//p[@class="airport"]//span')

        for index in range(len(elements)):
            s = index * 2
            e = s + 1
            air_info = {
                'airline': airline_element[index].text,
                'flight': flight_element[s].text + ' ' + flight_element[e].text,
                'depart_time': depart_time_element[index].text,
                'arrive_time': arrive_time_element[index].text,
                'space_time': space_time_element[index].text,
                'depart_airport': depart_airport_element[s].text + depart_airport_element[e].text,
                'arrive_airport': arrive_airport_element[s].text + arrive_airport_element[e].text
            }
            air.append(air_info)

        for value in air:
            self.__log.debug(value)
        # self.__log.debug(air)
