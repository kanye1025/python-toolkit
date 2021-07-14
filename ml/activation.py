
import numpy as np
import sklearn

class Activation:
    
    @classmethod
    def sigmoid(cls,x):
        x = np.asarray(x)
        
        return 1. / (1. + np.exp(-x))
    
    
    @classmethod
    def softmax(cls,x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()
    
    
    
    
    


