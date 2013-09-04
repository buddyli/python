#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import hashlib

def md5(str):
    m = hashlib.md5(str)
    m.digest()
    return m.hexdigest()