#-*- coding:utf-8 -*-
"""
工具类
"""


def repalce_url(url, str_from, str_to, str_time):
    return url.replace('#{from}', str_from).replace('#{to}', str_to).replace('#{time}', str_time)
