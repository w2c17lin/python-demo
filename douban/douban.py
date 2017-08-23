#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import tojson
import dao
import log
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 时间格式
ISOTIMEFORMAT = '%Y-%m-%d %X'
# 豆瓣的热门标签
tags = ('爱情', '动画', '剧情', '科幻', '动作', '经典', '悬疑', '青春', '犯罪', '人性', '美剧', '惊悚', \
	'文艺', '日剧', '法国', '韩国', '温情', '搞笑', '纪录片', '励志', '成长', '恐怖', '战争', '奇幻', \
	'短片', '人生', '黑色幽默', '魔幻', '动漫', '亲情', '心理', '传记', '冒险', '情色', '历史', '感人', \
	'暴力', '动画短片', '家庭', '音乐', 'TVB', '童年', '灾难', '周星驰', '宫崎骏', '浪漫', 'BBC', '黑帮', \
	'感动', '女性', '武侠', '漫画改编', '古装', '3D', '推理', '同志', '二战', '校园', '动画片', '政治', \
	'同性', '史诗', '小说改编', '警匪', '烂片', '童话', '血腥','吸血鬼', '迪斯尼', '宗教', '特工', '王家卫', \
	'儿童', '友情', '剧场版', 'JohnnyDepp', '梦工厂', '岩井俊二', '动物', '梁朝伟', '张艺谋', '黑色', \
	'童年回忆', '梦想', '名著改编', '美食', '伦理', '尼古拉斯·凯奇', '信念', '超级英雄', '冯小刚', \
	'斯皮尔伯格', 'アニメ', '欧洲', '成龙', '奥斯卡', '刘德华', '恶搞', '生活', '自由', '社会', '歌舞', \
	'张国荣', 'pixar', 'HBO', 'Marvel', '黑白', '姜文', '公路', '杜琪峰', '李连杰', '间谍', '音乐剧', '丧尸', \
	'cult', '葛优', '徐克', '西部', '真人秀', '1990s', '治愈系', '卡通', '柯南', '哈利波特', '俄罗斯', \
	'北野武', '自然', '连续剧', '古天乐', '僵尸', '李安', '2010s', '真实事件改编', '迪士尼', '综艺', \
	'TimBurton', '灵异', '独立电影', '桂纶镁', '二次元', '恐怖片', '周迅', 'Anime', '周润发', '震撼', \
	'摇滚', '漫威', 'TV', '温暖', '动画电影', '教育', '日剧SP', 'les', '日劇', '金城武', 'Disney', '治愈', \
	'旅行', '爱尔兰', '情感', '瑞典', '刘青云', '舒淇', 'OVA', '默片', '时尚')
log = log.Log('douban_logs')
dao = dao.Dao(log)

tag_num = len(tags)
tag = 4
# 每次请求的开始,每次加20
start = 19780
log.i(u"开始爬取数据.")
while True:
	if tag >= tag_num:
	# 如果所有标签都爬取完成就退出
		log.i(u"所有标签爬取完成！！！")
		break
	url = 'https://api.douban.com/v2/movie/search?tag=' + tags[tag] + '&start=' + str(start)
	request = urllib2.Request(url)
	try:
		response = urllib2.urlopen(request)
		data = response.read().decode("utf-8")
		if (tojson.get_len(data) == 0):
			# 一个标签爬取完成
			log.i(u"当前类型: %s爬取完毕, 一共%d条目." % (tags[tag], start))
			start = 0
			tag += 1
		else:
			# 一页数据爬取完成
			tojson.save_data(data, dao)
			log.i(u"获取类型为%s, Num = %d." % (tags[tag], start))
			start += 20
			time.sleep(10)
	except Exception, e:
		log.e(u"出现错误，错误信息: %s:%s" % (Exception, e))
		log.i(u"休眠十分钟后重试......")
		time.sleep(600);
