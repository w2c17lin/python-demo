# -*- coding:utf-8 -*-
# 贴吧的帖子,最后保存在一个文件里面
import urllib
import urllib2
import re
from StringUtil import Tool

class BDTB():
	def __init__(self, baseUrl, seeLz):
		self.baseUrl = baseUrl
		self.seeLz = '?see_lz=' + str(seeLz)
		self.tool = Tool()
		self.floor = 1
		self.defaultTitle = u'百度贴吧'
		self.file = None

	def getPage(self, pageNum):
		try:
			url = self.baseUrl + self.seeLz + "&pn=" + str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			return response.read().decode('utf-8')
		except urllib2.URLError, e:
			if hasattr(e, 'reason'):
				print u"connect error...", e.reason
				return None

	def getTitle(self, page):
		pattern = re.compile(r'<h3 class="core_title_txt pull-left text-overflow  " title=".*?" style="width: 396px">(.*?)</h3>', re.S)
		result = re.search(pattern, page)
		if result:
			return result.group(1).strip()
		else:
			return None

	def getPageNum(self, page):
		pattern = re.compile(r'<li class="l_reply_num" style="margin-left:8px" ><span class="red" style="margin-right:3px">.*?<span class="red">(.*?)</span>', re.S)
		result = re.search(pattern, page)
		if result:
			return result.group(1).strip()
		else:
			return None

	def getContent(self, page):
		pattern = re.compile(r'<div id="post_content_.*?>(.*?)</div>', re.S)
		items = re.findall(pattern, page)
		contents = []
		for item in items:
			content = '\n' + self.tool.replace(item) + '\n'
			contents.append(content.encode('utf-8'))
		return contents

	def setFileTitle(self, title):
		if title is not None:
			self.file = open(title + '.txt', 'w+')
		else:
			self.file = open(self.defaultTitle + '.txt', 'w+')

	def writeData(self, contents):
		for item in contents:
			floorLine = "\n" + str(self.floor) + u'--------------------------------------------\n';
			self.file.write(floorLine)
			self.file.write(item)
			self.floor += 1

	def getStart(self):
		page = self.getPage(1)
		pageNum = self.getPageNum(page)
		title = self.getTitle(page)
		self.setFileTitle(title)
		print u'开始抓取数据'
		for i in range(1, int(pageNum) + 1):
			print u'第' + str(i) + u'页数据'
			contents = self.getContent(self.getPage(i))
			self.writeData(contents)
		print u'抓取成功'

baseUrl = 'http://tieba.baidu.com/p/3138733512'
tb = BDTB(baseUrl, 1)
tb.getStart()