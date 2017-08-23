#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import dao
import log
import fromjson
import time

id = 0

log = log.Log('bilibili_logs', False)
dao = dao.Dao()
# 8000000
while (id < 20):
	try:
		url = 'http://api.bilibili.com/archive_stat/stat?aid=' + str(id)
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		data = response.read().decode("utf-8")
		res = fromjson.from_json(data)
		if res != False:
			dao.insert(id, res['view'], res['danmaku'], res['reply'], res['favorite'], \
				res['coin'], res['share'], res['now_rank'], res['his_rank'])
			log.i(u"插入id = %d, 成功." % (id))
		id += 1
	except Exception, e:
		log.e(u"%s:%s" % (Exception, e))
		log.i(u"休眠十分钟后重试......")
		time.sleep(600);
log.i(u"所有数据抓取完毕id = %d" % (id))
