#!/usr/bin/python
# -*- coding:utf-8 -*-
'''日志模块, 把日志以日期的形式存在文件中
用logdir_name指定log存放目录, 默认为当前的logs文件夹
日志级别error, warm, info, debug'''
import os
import time

# 日期格式
DATE_FORMAT = '%Y_%m_%d'
# 时间格式
TIME_FORMAT = '%Y-%m-%d %X'


class Log():
    def __init__(self, logdir_name='logs'):
        """
        初始化方法,默认log文件夹为当前文件下的logs,默认缓存次数为30
        """
        self.__file = None
        self.__log_path = './' + logdir_name
        self.__file_name = time.strftime(DATE_FORMAT, time.localtime())
        self.__mkdir()

    def error(self, info, tag='unknown'):
        self.__write_log(info, tag, 'ERROR')

    def warn(self, info, tag='unknown'):
        self.__write_log(info, tag, 'WARN ')

    def info(self, info, tag='unknown'):
        self.__write_log(info, tag, 'INFO ')

    def debug(self, info, tag='unknown'):
        self.__write_log(info, tag, 'DEBUG')

    def close(self):
        if self.__file != None:
            self.__file.close()

    def __write_log(self, info, tag, level):
        date = time.strftime(DATE_FORMAT, time.localtime())
        if self.__file == None:
            self.__mkfile()  # 如果是第一次写入，就新建文件
        elif date != self.__file_name:
            self.__mkfile()  # 如果日期不对应，就新建文件
        str = '[' + level + ']' + '[' + tag + ' ' + \
            time.strftime(TIME_FORMAT, time.localtime()) + '] - ' + info
        self.__file.write(str + '\n')  # 写log内容
        print(str)
        self.__file.flush()  # 立即写入文件

    def __mkdir(self):
        is_exists = os.path.exists(self.__log_path)  # 新建文件夹
        if not is_exists:
            os.makedirs(self.__log_path)

    def __mkfile(self):
        """
        新建当前日期的文件
        """
        self.close()
        self.__file_name = time.strftime(DATE_FORMAT, time.localtime())
        self.__file = open(self.__log_path + '/' + self.__file_name + '.log',
                           mode='a', encoding='utf-8')

    def __del__(self):
        self.close()  # 关闭文件
