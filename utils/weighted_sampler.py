import random


class   WeightedSampler:
	
	def __init__(self,samples,weights = None):
		'''
		
		:param samples:  list or dict  ,if samples is dict then weights is Nones
		:param weights:  list only when samples is list,otherwise is None
		'''
		
		if weights:
			l =  zip(samples,weights)
		else:
			l =  samples.items()

		sum = 0.0
		self.l = []
		for (sample,weight) in sorted(l,key=lambda x:x[1],reverse=True):
			sum+=weight
			self.l.append((sample,sum))
		self.sum = sum
		
	def sample(self,count = 1):
		if count == 1:
			return self.choice()
		probs = []
		ret = []
		for i in range(count):
			prob =random.uniform(0.0,self.sum)
			print(prob)
			for sample,weight in self.l:
				if weight>=prob:
					ret.append( sample)
					break
		return ret
					
	def choice(self):
		prob = random.uniform(0.0,self.sum)
		
		for sample,weight in self.l:
			if weight>=prob:
				return sample
	
	
if __name__ == '__main__':
	s = []
	w = []
	for i in range(4):
		s.append(i)
		w.append(i)
	ws = WeightedSampler(s,w)
	for i in ws.sample(10):
		print(i)
	print(ws.choice())