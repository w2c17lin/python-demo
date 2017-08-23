#!/usr/bin/python
# -*- coding:utf-8 -*-
import MySQLdb
import log

class Dao(object):
	def __init__(self, log):
		self.db = MySQLdb.connect("127.0.0.1", "root", "qwe123", "douban", charset = "utf8")
		self.cursor = self.db.cursor()
		self.log = log

	def __del__(self):
		self.db.close()

	def insertData(self, id = None, rating_max = None, rating_min = None, rating_stars = None, rating_average = None, genres = None, title = None, year = None, alt = None, original_title = None, collect_count = None):
		if self.isRepeat(id, title):
			# 判断数据库里面是否已经保存了该电影,如果没有保存就保存
			return
		sql = 'insert into movies(id, rating_max, rating_min, rating_stars, rating_average, genres, title, year, alt, original_title, collect_count) \
			values ("%s", "%.2f", "%.2f", "%s", "%.2f", "%s", "%s", "%s", "%s", "%s", "%.2f")' % \
			(id, rating_max, rating_min, rating_stars, rating_average, genres, title, year, alt, original_title, collect_count)
		try:
			self.cursor.execute(sql)
			# 提交事务
			self.db.commit()
			self.log.i(u"插入id=%s, title=%s, 成功." % (id, title))
		except Exception, e:
			# 出错，回滚
			self.db.rollback()
			self.log.e(u"插入id=%s, title=%s, 失败.\n%s:%s" % (id, title, Exception, e))

	def isRepeat(self, id, title):
		# 判断数据库里面是否已经保存了该电影
		sql = 'select count(*) from movies where id = %s' % (id)
		self.cursor.execute(sql)
		results = self.cursor.fetchall()
		if results[0][0] == 0:
			return False
		else:
			self.log.i(u"出现重复项id=%s, title=%s." % (id, title))
			return True
