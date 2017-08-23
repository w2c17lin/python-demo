#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import dao

def save_data(data, dao):
	in_json = json.loads(data)
	for i in range(len(in_json['subjects'])):
		# 取数据
		id = in_json['subjects'][i]['id']
		rating_max = in_json['subjects'][i]['rating']['max']
		rating_min = in_json['subjects'][i]['rating']['min']
		rating_stars = in_json['subjects'][i]['rating']['stars']
		rating_average = in_json['subjects'][i]['rating']['average']
		genres = ''
		for j in range(len(in_json['subjects'][i]['genres'])):
			if j == len(in_json['subjects'][i]['genres']) - 1:
				genres += in_json['subjects'][i]['genres'][j]
			else:
				genres += in_json['subjects'][i]['genres'][j] + ','
		title = in_json['subjects'][i]['title'].replace('\"', '')
		year = in_json['subjects'][i]['year']
		alt = in_json['subjects'][i]['alt']
		original_title = in_json['subjects'][i]['original_title'].replace('\"', '')
		collect_count = in_json['subjects'][i]['collect_count']
		dao.insertData(id, rating_max, rating_min, rating_stars, rating_average, \
			genres, title, year, alt, original_title, collect_count)

def get_len(data):
	# 获取一页数据的电影个数
	in_json = json.loads(data)
	return len(in_json['subjects'])
