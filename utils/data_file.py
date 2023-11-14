# -*- coding:utf-8 -*-
import json
import os
import pickle

import pandas as pd

from .os_tool import make_sure_dir
from .os_tool import enum_lines
from .os_tool import list_dir_all_files
from tqdm import tqdm
import pandas as np
class DataFile:
    

    @classmethod
    def load_json_dir_to_list(cls,path,limit=None,ite = True):
        
        paths = [file_path for _,file_path in list_dir_all_files(path)]
        
        return DataFile.load_json_files_to_list(paths,limit = limit,ite = ite)

    @classmethod
    def _load_json_files_to_list(cls,paths,limit=None,):
        ret = []
        for path in paths:
            ret.extend(DataFile._load_json_file_to_list(path, limit))
            if limit and len(ret) >= limit:
                return ret
        return ret
    
    
    @classmethod
    def _load_json_files_to_list_ite(cls,paths,limit=None,):
        i = 0
        for path in paths:
            for obj in DataFile._load_json_file_to_list_ite(path, limit):
                yield obj
                i += 1
                if limit and i >= limit:
                    return
    @classmethod
    def load_json_files_to_list(cls,paths,limit=None,ite = True):
        if ite:
            return cls._load_json_files_to_list_ite(paths,limit)
        else:
            return cls._load_json_files_to_list(paths, limit)
            
        
    @classmethod
    def load_json_file_to_list(cls,path,limit = None,ite = True):
        if ite:
            return DataFile._load_json_file_to_list_ite(path,limit = limit)
        else:
            return DataFile._load_json_file_to_list(path,limit = limit)

    @classmethod
    def _load_json_file_to_list(cls, path,limit = None):
        ret = []
        for line in enum_lines(path):
            try:
                obj = json.loads(line)
            except:
                print('error load json line :')
                print(line)
            ret.append(obj)
            if limit and len(ret)>=limit:
                return ret
        return ret
        
    @classmethod
    def _load_json_file_to_list_ite(cls, path,limit = None,):
        i = 0
        for line in enum_lines(path):
            try:
                obj = json.loads(line)
                yield obj
                if limit:
                    i += 1
                    if i>= limit:
                        break
            except:
                print('error load json line :')
                print(line)


    @classmethod
    def load_json_file_to_dict(cls, path, key,fields = None,filter={},key_lower = False,limit = None):
        '''
        
        :param path:
        :param key:
        :param fields: 返回的字段  [] 或 str，
        :return:
        '''
        ret = {}
        for line in enum_lines(path):
            obj = json.loads(line)
            if filter:
                b_satisfy = True
                for k, v in filter.items():
                    if obj[k] != v:
                        b_satisfy = False
                        continue  # contniue for k,v in filter.items()
                if not b_satisfy:
                    continue  # continue for line in enum_lines
            if not fields:
                if key_lower:
                    ret[obj[key].lower()] = obj
                else:
                    ret[obj[key]] = obj
            else:
                if type(fields) == str:
                    if key_lower:
                        ret[obj[key].lower()] = obj[fields]
                    else:
                        ret[obj[key]] = obj[fields]
                else:
                    obj_with_field = {}
                    for field in fields:
                        obj_with_field[field] = obj[field]
                    if key_lower:
                        ret[obj[key].lower()] = obj_with_field
                    else:
                        ret[obj[key]] = obj_with_field
            if limit and i >= limit:
                break
        return ret
        
    @classmethod
    def load_int_dict(cls,path,split = ' '):
        d = dict()
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                k,v = line.strip().split(split)
                v = int(v)
                d[k] = v
        return d


    @classmethod
    def load_words_set(cls,path):
        s = set()
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                s.add( line.strip())
        return s

    @classmethod
    def load_string_list(cls, path):
        l = list()
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    l.append(line.strip())
        return tqdm(l,desc=path)

    @classmethod
    def _load_words_list(cls, path):
        l = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                l.append(line.strip())
            return l

    @classmethod
    def _load_words_list_ite(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                yield line.strip()
                
        
        
    @classmethod
    def load_words_list(cls, path,ite = True):
        if ite:
            return cls._load_words_list_ite(path)
        else:
            return cls._load_words_list(path)


    @classmethod
    def load_str_dict(cls, path, split=' ',lower_k = False,lower_v = False):
        d = dict()
    
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    if line.strip():
                        k, v = line.strip().split(split)
                    if lower_k:
                        k = k.lower()
                    if lower_v:
                        v = v.lower()
                    d[k] = v
                except:
                    print(line)
        return d

    @classmethod
    def _load_tuple_list(cls, path, split=' '):
        ret = []
        for line in enum_lines(path):
            try:
                if line.strip():
                    ret.append(line.strip('\n').split(split))
            except:
                print(line)
        return ret

    @classmethod
    def _load_tuple_list_ite(cls, path, split=' '):
        for line in enum_lines(path):
            try:
                if line.strip():
                    yield line.strip('\n').split(split)
            except:
                print(line)

        
    @classmethod
    def load_tuple_list(cls, path, split=' ',ite=False):
        if ite:
            return cls._load_tuple_list_ite(path,split)
        else:
            return cls._load_tuple_list(path,split)
    
    
    @classmethod
    def load_pickle(cls,pickle_path):
        with open(pickle_path,'rb') as f:
            return pickle.load(f)

    @classmethod
    def load_pickles_dir(cls, dir,ext = None,ret_name = False):
        ret = []
        for file_name in os.listdir(dir):
            name, ext_ = os.path.splitext(file_name)
            if ext and ext!= ext_:
                continue
            if ret_name:
                ret.append((name,DataFile.load_pickle(os.path.join(dir, file_name))))
            else:
                ret.append(DataFile.load_pickle(os.path.join(dir,file_name)))
        return ret
    
    
        
        
    @classmethod
    def save_picke(cls,obj,pickle_path):
        dir,_ = os.path.split(pickle_path)
        make_sure_dir(dir)
        with open(pickle_path, 'wb') as f:
            pickle.dump(obj, f)
            
            
    @classmethod
    def load_lines_from_dir(cls,dir_path):
        for file_name,file_path in list_dir_extend(dir_path):
            for line in DataFile.load_string_list(file_path):
                yield line
    
    @classmethod
    def create_file_to_wirte(cls,file_path,encoding='utf-8'):
        f = open(file_path,'w',encoding=encoding)
        return f
    @classmethod
    def write_obj_to_json_file_line(cls,f,obj):
        l = f'{json.dumps(obj,ensure_ascii= False)}\n'
        f.write(l)

    @classmethod
    def write_list_to_file_line(cls, f, l,split = ','):
        l = split.join([str(i) for i in l])
        l+='\n'
        f.write(l)

    @classmethod
    def write_single_obj_to_json_file_path(cls, file_path, obj):
        with  cls.create_file_to_wirte(file_path) as f:
            json.dump(obj,f,ensure_ascii=False)
        
    @classmethod
    def load_json_file(cls,file_path):
        with open(file_path,'r',encoding='utf-8') as f:
            return json.load(f)

    @classmethod
    def split_train_test_lines(self,file_path,train_path,test_path,test_size):
        from sklearn.model_selection import train_test_split
        lines = [line  + '\n' for line in self.load_string_list(file_path)]
        X_train, X_test = train_test_split(lines, test_size=test_size)
        with self.create_file_to_wirte(train_path) as f:
            f.writelines(X_train)
        
        with self.create_file_to_wirte(test_path) as f:
            f.writelines(X_test)

    @classmethod
    def load_dict_from(cls,file_path,key_filed,value_filed):
        df = pd.read_csv(file_path)
        return {k:v for k,v in zip(df[key_filed],df[value_filed])}

