#-*- coding:utf-8 -*-
import random
"""
工具类
"""


def repalce_url(url, str_from, str_to, str_time):
    return url.replace('#{from}', str_from).replace('#{to}', str_to).replace('#{time}', str_time)


def random_num(last_size, page_num=1, page_size=20, num=10):
    """
    计算所有数据范围内的num个随机数,数据小num个的返回数据长度的数量

    @param last_size 最后一页大小
    @param page_num 页码数量 默认0
    @param page_size 每页数量 默认20(依据去哪儿每页数量)
    @param num 产生的随机数个数 默认10
    """
    res = []
    max = ((page_num - 1) * page_size) + last_size
    if max < num:
        num = max
    while len(res) < num:
        n = random.randint(0, max - 1)
        if n not in res:
            res.append(n)
    res = sorted(res, reverse=True)
    return res
