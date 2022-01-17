from .label_oriented_sampler import LabelOrientedSamplerBase
from collections import defaultdict
import random
import math
from ...utils.weighted_sampler import WeightedSampler
class LabelSameSampler(LabelOrientedSamplerBase):
	
	def __init__(self, labels, batch_size, cls_min_count=1, data_size=None):
		assert batch_size*10<cls_min_count ,f'cls_min_count ({cls_min_count})  must be ten times larger than batch_size ({batch_size}) in Label Same mode'
		super().__init__(labels, batch_size, cls_min_count, data_size)
		label_prob = defaultdict(float)
		for label ,samples in self.data_cls.items():
			label_prob[label] = math.log(len(samples))  #平衡样本数量
		self.label_sampler = WeightedSampler(label_prob)
  
	
	def __iter__(self):
		count = 0
		while count < self.data_size:
			label = self.label_sampler.choice()
			for sample in random.sample(self.data_cls[label],self._batch_size):
				yield sample
				count+=1





