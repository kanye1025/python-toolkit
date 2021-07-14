# -*- coding: utf-8 -*-
import time
import hashlib
import pickle

cache = {}


class cached(object):
	'''
	内存缓存装饰器
	使用方法：直接在函数上加  @cache(seconds),
			 seconds内只计算一次返回值，
	'''
	def __init__(self,duration = None):
		self.duration = duration

	def is_obsolete(self,entry, duration):
		if not duration:return False
		d = time.time() - entry['time']
		return d > duration

	def compute_key(self,function, args, kwargs):
		key = pickle.dumps((function.__hash__(), args, kwargs))
		return hashlib.sha1(key).hexdigest()

	def __call__(self,function):
		def __memorize(*args, **kwargs):
			key = self.compute_key(function, args, kwargs)
			if key in cache and not self.is_obsolete(cache[key], self.duration):
				return cache[key]['value']
			result = function(*args, **kwargs)
			cache[key] = {'value': result, 'time': time.time()}
			return result
		return __memorize