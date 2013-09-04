#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import re

def test(strs):
	return True if re.match('[是,Y,y]', strs) is not None else False


if __name__ == '__main__':
	print test("是")
	print test("是的")
	print test("y")
	print test("YES")
	print test("靠")
