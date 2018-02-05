#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import pymysql

MYSQL_URL = '127.0.0.1'  # 数据库链接
MYSQL_DATABASE = 'yanji_web'  # 数据库名字
MYSQL_USERNAME = 'root'  # 数据库账号
MYSQL_PASSWORD = 'root'  # 数据库密码


class MySQLDao():
    def __init__(self):
        self.__log = logging.getLogger('app.dao')
        self.__db = pymysql.connect(
            MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE, charset="utf8")
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.close()

    def insert(data):
        """
        插入数据

        @param data 要插入的数据,字典类型
        """
        pass

    def close(self):
        self.__db.close()
