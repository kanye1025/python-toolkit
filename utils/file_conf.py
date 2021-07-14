# -*- coding:utf-8 -*-
from configparser import ConfigParser
from collections import defaultdict


'''
可以使用属性(.)访问配置文件下的section和key，并直接取值和赋值
例如:
conf = FileConf(file_name)
value = conf.section_name.key
conf.section_name.key = value
'''
class FileConf:
    conf_dict = defaultdict(ConfigParser)
    def __init__(self, file_path):
        if file_path not in self.conf_dict:
            self.conf_dict[file_path].read(file_path)
        self.cp = self.conf_dict[file_path]
        self.secs = dict()
        
    def __getattr__(self, name):
        if name not in self.secs:
            self.secs[name] = FileSection(name,self.cp)
        return self.secs[name]
    
    


class FileSection(object):
    def __init__(self,name,cp):
        self.__sec_name__ = name
        self.__cp__ = cp
        
    def __getattr__(self, key):
        #if key not in ('getint','getfloat','getboolean','cp','name'):
        if '__'not in key:
            return self.__cp__.get(self.__sec_name__, key)
        else:
            return object.__getattr__(self,key)
    
    def __setattr__(self, key, value):
        if '__' not in key:
            self.__cp__.set(self.__sec_name__,key,value)
        else:
            object.__setattr__(self,key,value)
    
    def get(self,key):
        return self.__cp__.get(self.__sec_name__,key)
    
    def getint(self,key):
        return self.__cp__.getint(self.__sec_name__,key)
    
    def getfloat(self,key):
        return self.__cp__.getfloat(self.__sec_name__,key)
    
    def getboolean(self,key):
        return self.__cp__.getboolean(self.__sec_name__,key)
    
    
    