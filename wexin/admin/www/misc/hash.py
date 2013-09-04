#!/usr/bin/env python
# -*- encoding:utf-8 -*-

def md5(str):
    import hashlib
    m = hashlib.md5(str)
    m.digest()
    return m.hexdigest()