#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import dao
import types

def from_json(data):
	in_json = json.loads(data)
	if in_json['code'] == 0:
		res = {}
		res['view'] = in_json['data']['view']
		if type(res['view']) != types.IntType:
			res['view'] = 0
		res['danmaku'] = in_json['data']['danmaku']
		if type(res['danmaku']) != types.IntType:
			res['danmaku'] = 0
		res['reply'] = in_json['data']['reply']
		if type(res['reply']) != types.IntType:
			res['reply'] = 0
		res['favorite'] = in_json['data']['favorite']
		if type(res['favorite']) != types.IntType:
			res['favorite'] = 0
		res['coin'] = in_json['data']['coin']
		if type(res['coin']) != types.IntType:
			res['coin'] = 0
		res['share'] = in_json['data']['share']
		if type(res['share']) != types.IntType:
			res['share'] = 0
		res['now_rank'] = in_json['data']['now_rank']
		if type(res['now_rank']) != types.IntType:
			res['now_rank'] = 0
		res['his_rank'] = in_json['data']['his_rank']
		if type(res['his_rank']) != types.IntType:
			res['his_rank'] = 0
		return res
	else:
		return False
