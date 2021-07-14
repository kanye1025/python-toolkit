# -*- coding:utf-8 -*-
from collections import Iterable



class Struct(dict):
    '''
    支持直接使用属性访问field的dict，支持多级访问。
    '''
    def update(self,E = None, ** F):
        if F:
            for k,v in F.items():
                if type(v) == dict:
                    F[k] = Struct._proc_sub_struct(v)
        dict.update(self, E,**F)
    @classmethod
    def _proc_sub_struct(cls,value):
        if type(value) == dict:
            value = Struct(**value)
        elif isinstance(value, Iterable) and type(value) !=str and type(value) !=Struct:
            value = type(value)([cls._proc_sub_struct(sub_v) for sub_v in value])
        return value
        
    def __init__(self, **fields):
        for field,value in fields.items():
            self[field] =Struct._proc_sub_struct(value)
    
    
    
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self,item)
        except KeyError:
            if type(item) == str and '.' in item:
                obj = self
                keys = item.split('.')
                for k in keys[:-1]:
                    if k not in obj:
                        obj[k] = Struct()
                    obj = obj[k]
                return obj[keys[-1]]
            else:
                raise AttributeError(item)
            
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            
            raise AttributeError(name)

    def __setitem__(self, key, value):
        if type(key) == str and '.' in key:
            obj = self
            keys = key.split('.')
            for k in keys[:-1]:
                if k not in obj:
                    obj[k] = Struct()
                obj = obj[k]
            obj[keys[-1]] = value
        else:
            dict.__setitem__(self,key,value)
     
            
            
    def __setattr__(self, key, value):
        self[key] = value
        
    
    def __contains__(self,item):
        if dict.__contains__(self,item):
            return True
        elif type(item) == str and '.' in item:
            obj = self
            for k in item.split('.'):
                if k in obj:
                    obj = obj[k]
                else:
                    return False
            return True
        else:
            return False
        
        
    @classmethod
    def loads(cls,s):
        return Struct(**eval(s))


if '__main__' == __name__:
    s = Struct()
    s['a.b.c'] = 1
    print(s.a.b.c)
    print(s['a.b.c'])
    



