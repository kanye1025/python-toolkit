from torch.utils.data import Sampler
from collections import defaultdict
import  random


class LabelEqualSampler(Sampler):

    def __init__(self, labels,batch_size,cls_min_count = 0):
        self.data_size = len(labels)//batch_size *batch_size
        
    
        data_cls = defaultdict(list)
        for idx, label in enumerate( labels):
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
        self.data_cls = data_cls
        
        self._batch_size = batch_size
        
    def __iter__(self):
        count = 0
        while count<self.data_size:
            labels = random.sample(self.data_cls.keys(), 1)
            #labels = random.choice(self.data_cls.keys())
            for label in labels:
                yield random.sample(self.data_cls[label],1)[0]
                count+=1
    
        
    def __len__(self):
        return self.data_size


    