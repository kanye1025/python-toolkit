#! /usr/bin/env python
# -*- coding: utf-8 -*-

import  math
import random
_ndigits_ = {}



def exact_round(number, ndigits=3):
    '''
    保留小数点后ndigits位
    返回截断后的number
    :param number:
    :param ndigits:
    :return:
    '''
    if ndigits not in _ndigits_:
        _ndigits_[ndigits] = math.pow(0.1,ndigits)*0.49
    return round(number + _ndigits_[ndigits], ndigits)
'''
以下三个函数适合处理以dict为行（dict-key 为field-name/col-name,dict-value 为 field-value/item-value）
以list或其他iterable对象为列的tabel（关系数据库常用表示，iterable（dict）或list(dict)），并对其进行聚合
'''
def sum_dict_list(dl,k):
    '''
    对字典list:dl的某一列求和
    返回字典dl中field-k的sum
    :param dl:
    :param k:
    :return:
    '''
    return sum(map(lambda x:x[k],dl))


def max_dict_list(dl,k):
    '''
    返回字典list中field-k的最大值
    :param dl:
    :param k:
    :return:
    '''
    return max(dl,key = lambda x:x[k])[k]

def min_dict_list(dl,k):
    '''
    返回字典list中field-k的最小值
    :param dl:
    :param k:
    :return:
    '''
    return min(dl,key = lambda x:x[k])[k]

def half_life(t,period):
    '''
    计算半衰期
    返回以period为半衰期经过时间t衰减后的比例
    :param num:
    :param period:
    :return:
    '''
    return math.pow(0.5, float(t)/float(period))


def choice_by_weight(samples,weights):
    total = sum(weights)
    v = random.uniform(0,total)
    cur = 0
    for sample,weight in zip(samples,weights):
        cur +=weight
        if cur>v:
            return sample
    return None


def choice_without_replacement(l):
    r = random.choice(l)
    l.remove(r)
    return r




from collections import defaultdict
def count_keys_frequency(keys_iter,is_sort = True,reverse = True):
    d = defaultdict(int)
    for key in keys_iter:
        d[key] +=1
    if is_sort:
        return sorted(d.items(),key=lambda x:x[1],reverse=reverse)
    else:
        return d.items()
        
#for ite
def batch_process_ret(ite,func,batch_size,pre_filter = None):
    batch = []
    for data in ite:
        if pre_filter:
            data = pre_filter(data)
        if data:
            batch.append(data)
            if len(batch) >= batch_size:
                yield func(batch)
                batch = []
    if batch:
        yield func(batch)
        
def batch_process_no_ret(ite,func,batch_size,pre_filter = None):
    batch = []
    for data in ite:
        if pre_filter:
            data = pre_filter(data)
        if data:
            batch.append(data)
            if len(batch) >= batch_size:
                func(batch)
                batch = []
    if batch:
        func(batch)

def batch_process(ite,func,batch_size,pre_filter = None,ret = True):
    if ret:
        return batch_process_ret(ite,func,batch_size,pre_filter)
    else:
        return batch_process_no_ret(ite,func,batch_size,pre_filter)

def percent_str_to_float(percent_str):
    percent_str = percent_str.replace('%', '')
    f = float(percent_str) / 100.0
    return f
