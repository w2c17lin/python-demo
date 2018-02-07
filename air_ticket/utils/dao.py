#!/usr/bin/python
# -*- coding:utf-8 -*-
import configparser
import logging
import time
from datetime import datetime

import pymysql

DB_SECTION = 'db'
URL_OPTION = 'url'
USERNAME_OPTION = 'username'
PASSWORD_OPTION = 'password'
DATABASE_OPTION = 'database'

INSERT_SQL = 'insert into air_ticket(source, airline, filght, depart_time, arrive_time, space_time, depart_airport, arrive_airport, price, create_time) \
    VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%d", "%s")'


class MySQLDao():
    def __init__(self, path):
        self.__log = logging.getLogger('app.dao')
        self.__db = self.__connect(path)
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.close()

    def __connect(self, path):
        """
        获取数据库链接

        @param path 配置文件
        """
        cf = configparser.ConfigParser()
        cf.read(path)
        url = cf.get(DB_SECTION, URL_OPTION)
        username = cf.get(DB_SECTION, USERNAME_OPTION)
        password = cf.get(DB_SECTION, PASSWORD_OPTION)
        database = cf.get(DB_SECTION, DATABASE_OPTION)
        return pymysql.connect(url, username, password, database, charset="utf8")

    def insert(self, data):
        """
        插入数据

        @param data 要插入的数据,字典类型
        """
        sql = 'insert into air_ticket(source, spider_time, airline, flight, depart_time, arrive_time, space_time, depart_airport, arrive_airport, price, create_time) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%d", "%s")' % \
            (data['source'], data['spider_time'].strftime("%Y-%m-%d %H:%M:%S"), data['airline'], data['flight'], data['depart_time'], data['arrive_time'],
             data['space_time'], data['depart_airport'], data['arrive_airport'], data['price'], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.__log.debug(sql)
        try:
            self.__cursor.execute(sql)
            self.__db.commit()
        except Exception as e:
            self.__log.error('插入数据库失败: %s' % e)

    def close(self):
        self.__db.close()
