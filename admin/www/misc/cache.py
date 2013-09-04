#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from setting import cache_path

cache_dir = cache_path

cache_opts = {
    'cache.data_dir': cache_dir + 'data',
    'cache.lock_dir': cache_dir + 'lock',
    'cache.regions': 'stock_data',

    'cache.stock_data.type': 'file',
    'cache.stock_data.data_dir': cache_dir + 'stock_data',
    'cache.stock_data.lock_dir': cache_dir + 'stock_lock',
    'cache.stock_data.expire': '3600',
}

cache = CacheManager(**parse_cache_config_options(cache_opts))