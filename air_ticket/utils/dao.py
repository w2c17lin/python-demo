#!/usr/bin/python
# -*- coding:utf-8 -*-
import configparser
import logging

import pymysql

DB_SECTION = 'db'
URL_OPTION = 'url'
USERNAME_OPTION = 'username'
PASSWORD_OPTION = 'password'
DATABASE_OPTION = 'database'


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
        pass

    def close(self):
        self.__db.close()
