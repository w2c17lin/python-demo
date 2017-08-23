#!/usr/bin/python
# -*- coding:utf-8 -*-
import MySQLdb
import log

class Dao(object):
	def __init__(self):
		self.db = MySQLdb.connect("127.0.0.1", "root", "qwe123", "bilibili", charset = "utf8")
		self.cursor = self.db.cursor()

	def __del__(self):
		self.db.close()

	def insert(self, id, view = 0, danmaku = 0, reply = 0, favorite = 0, coin = 0, \
		share = 0, now_rank = 0, his_rank = 0):
		sql = 'insert into avs(id, view, danmaku, reply, favorite, coin, share, now_rank, his_rank) \
			values ("%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d")' % \
			(id, view, danmaku, reply, favorite, coin, share, now_rank, his_rank)
		self.cursor.execute(sql)
		# 提交事务
		self.db.commit()
