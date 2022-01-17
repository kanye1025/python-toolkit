from .label_oriented_sampler import LabelOrientedSamplerBase

import  random


class LabelEqualSampler(LabelOrientedSamplerBase):

    def __init__(self, labels,batch_size,cls_min_count = 1,data_size = None):
        
        super().__init__(labels,batch_size,cls_min_count,data_size)
        
    def __iter__(self):
        count = 0
        sample_label_count = min(self._batch_size,self.label_count)
        while count<self.data_size:
            labels = random.sample(self.data_cls.keys(),sample_label_count)
            #labels = random.choice(self.data_cls.keys())
            for label in labels:
                yield random.choice(self.data_cls[label])
                count+=1
    
    




    