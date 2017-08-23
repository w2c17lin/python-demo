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
	def __init__(self, logdir_name = 'logs'):
		self.file = None
		self.log_path = './' + logdir_name
		self.file_name = time.strftime(DATE_FORMAT, time.localtime())
		self.mkdir()

	def __del__(self):
		# 关闭文件
		self.closefile()

	def mkdir(self):
		# 新建文件夹
		is_exists = os.path.exists(self.log_path)
		if not is_exists:
			os.makedirs(self.log_path)

	def closefile(self):
		if self.file != None:
			self.file.close()

	def mkfile(self):
		# 新建当前日期的文件
		self.closefile()
		self.file_name = time.strftime(DATE_FORMAT, time.localtime())
		self.file = open(self.log_path + '/' + self.file_name + '.log', 'a')

	def writelog(self, info, level):
		date = time.strftime(DATE_FORMAT, time.localtime())
		if self.file == None:
			# 如果是第一次写入，就新建文件
			self.mkfile()
		elif date != self.file_name:
			# 如果日期不对应，就新建文件
			self.mkfile()
		# 写log级别和日期
		self.file.write('[' + level + ']  ' + time.strftime(TIME_FORMAT, time.localtime()) + '\n')
		# 写log内容
		self.file.write(info.encode('utf-8') + '\n')
		# 立即写入文件
		self.file.flush()

	def e(self, info):
		self.writelog(info, 'ERROR')

	def w(self, info):
		self.writelog(info, 'WARM ')

	def i(self, info):
		self.writelog(info, 'INFO ')

	def d(self, info):
		self.writelog(info, 'DEBUG')
