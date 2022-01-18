from torch.utils.data import Sampler
from collections import defaultdict
import random


class LabelOrientedSamplerBase(Sampler):
	
	def __init__(self, labels, batch_size, cls_min_count=1, data_size=None):
		
		self.data_size = data_size if data_size else len(labels) // batch_size * batch_size
		
		data_cls = defaultdict(list)
		for idx, label in enumerate(labels):
			data_cls[label].append(idx)
		self._cur = 0
		del_labels = []
		self.labels = set()
		for label, data in data_cls.items():
			if len(data) < cls_min_count:
				del_labels.append(label)
			else:
				self.labels.add(label)
		for label in del_labels:
			data_cls.pop(label)
		self.label_count = len(data_cls)
		self.data_cls = data_cls
		print('label_count', self.label_count)
		if 'other' in self.data_cls:
			print('other count:', len(self.data_cls['other']))
		# print(self.data_cls)
		self._batch_size = batch_size
	
	def __iter__(self):
		pass
	
	def __len__(self):
		return self.data_size




