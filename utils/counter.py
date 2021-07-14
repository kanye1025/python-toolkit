# -*- coding: utf-8 -*-

class Counter():

	def __init__(self):
		self.count_dict = {}

	def add(self,key,count = 1):
		if key not in self.count_dict:
			self.count_dict[key] = 0
		self.count_dict[key]+=count

	def counts_dict(self):
		return self.count_dict

	def counts_list(self,desc = True):
		ls = [(k,v)for k,v in self.count_dict.items()]
		return sorted(ls,key=lambda x:x[1],reverse=desc)

