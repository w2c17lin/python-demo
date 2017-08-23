# -*- coding:utf-8 -*-

import re

class Tool():
	# 去除img标签，7位长空格
	removeImg = re.compile(r'<img.*?>| {7}|')
	# 删除超链接标签
	removeAddr = re.compile(r'<a.*?>|</a>')
	# 把换行的标签替换为/n
	replaceLine = re.compile(r'<tr>|<div>|</div>|</p>')
	# 将表格制表<td>替换为\t
	replaceTD = re.compile(r'<td>')
	# 把段落开头换为\n加两个空格
	replacePara = re.compile(r'<p.*?>')
	# 将换行符或双换行符替换为\n
	replaceBR = re.compile(r'<br><br>|<br>')
	# 将其余标签剔除
	removeExtraTag = re.compile(r'<.*?>')

	def replace(self, x):
		x = re.sub(self.removeImg, "", x)
		x = re.sub(self.removeAddr, "", x)
		x = re.sub(self.replaceLine, "\n", x)
		x = re.sub(self.replaceTD, "\t", x)
		x = re.sub(self.replacePara, "\n  ", x)
		x = re.sub(self.replaceBR, "\n", x)
		x = re.sub(self.removeExtraTag, "", x)
		# 将前后多余内容去掉
		return x.strip()
