#!/usr/bin/env python
# -*- encoding:utf-8 -*-

def create_pagenation(total, page, size):
    '''生成分页是数据'''
    t_page = total/float(size)
    t_page = t_page + 1 if t_page > int(t_page) else t_page
    min_page = page - 5 if page >5 else 1
    max_page = min_page + 10 if min_page + 10 <= t_page else t_page
    if max_page == t_page:
        min_page = t_page - 10 if t_page > 10 else 1
    pages = range(int(min_page), int(max_page) + 1)
    return pages
