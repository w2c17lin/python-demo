#!/usr/bin/python
# -*- coding:utf-8 -*-
'''日志模块, 把日志以日期的形式存在文件中
用logdir_name指定log存放目录, 默认为当前的logs文件夹
用error指定是否将error日志写到新的文件中
日志级别error, warm, info, debug'''
import os
import time

# 日期格式
DATE_FORMAT = '%Y_%m_%d'
# 时间格式
TIME_FORMAT = '%Y-%m-%d %X'

ERROR = 'ERROR'
WARM = 'WARM'
INFO = 'INFO'
DEBUG = 'DEBUG'

class Log():
	def __init__(self, log_dir = 'logs', error = True):
		self.log_dir = './' + log_dir
		self.mkdir()
		self.error = error
		self.mkfile()

	def __del__(self):
		# 关闭文件
		self.closefile()

	def mkdir(self):
		# 新建文件夹
		is_exists = os.path.exists(self.log_dir)
		if not is_exists:
			os.makedirs(self.log_dir)

	def closefile(self):
		try:
			self.info_file.close()
			self.error_file.close()
		except Exception, e:
			pass

	def mkfile(self):
		# 新建当前日期的文件
		self.closefile()
		self.file_name = time.strftime(DATE_FORMAT, time.localtime())
		self.info_file = open(self.log_dir + '/' + self.file_name + '_info.log', 'a')
		if self.error:
			self.error_file = open(self.log_dir + '/' + self.file_name + '_error.log', 'a')

	def writelog(self, info, level):
		date = time.strftime(DATE_FORMAT, time.localtime())
		# 如果日期不对应就新建文件
		if date != self.file_name:
			self.mkfile()
		if self.error and level == ERROR:
			# 写error级别日期信息
			self.error_file.write('[' + level + ']  ' + time.strftime(TIME_FORMAT, time.localtime()) + \
				'  ' + info.encode('utf-8') + '\n')
			# 立即写入文件
			self.error_file.flush()
		# 写log级别日期信息
		self.info_file.write('[' + level + ']  ' + time.strftime(TIME_FORMAT, time.localtime()) + \
			'  ' + info.encode('utf-8') + '\n')
		# 立即写入文件
		self.info_file.flush()

	def e(self, info):
		self.writelog(info, ERROR)

	def w(self, info):
		self.writelog(info, WARM)

	def i(self, info):
		self.writelog(info, INFO)

	def d(self, info):
		self.writelog(info, DEBUG)
