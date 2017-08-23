# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
from StringUtil import Tool
reload(sys)
sys.setdefaultencoding('utf-8')

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
stringTool = Tool()

try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	pattern = re.compile(r'<div class="author clearfix".*?alt="(.*?)"/>.*?<div class="content".*?<span>(.*?)</span>.*?<span class="stats-vote"><i class="number">(.*?)</i>', re.S)
	items = re.findall(pattern, content)
	for item in items:
		print u"作者:", item[0]
		print u"内容:", stringTool.replace(item[1])
		print u"赞:", item[2]
		print "\n"
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason
