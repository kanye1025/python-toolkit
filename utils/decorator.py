#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
#from raven import Client
import time


#client = Client('https://2a68c0b19497426bb25fb7e313333f5f:32828408c5e24061b6c3df94daf8625b@sentry.hundun.cn/42')


class lazy_property(object):
    # 延迟加载

    def __init__(self, func):
        self.func = func
        self.value = None

    def __get__(self, obj, cls):
        if self.value is None:
            if obj is None:
                self.value = self.func(cls)
            else:
                self.value = self.func(obj)
        return self.value

    def __set__(self, instance, value):
        self.value = value


def calc_duration(func):
    # 打印函数执行时长
    def inner(*args, **kwargs):
        s = datetime.datetime.now()
        func(*args, **kwargs)
        e = datetime.datetime.now()
        print(func.__name__, ' 运行时长: ', (e-s).microseconds, 'ms')
    return inner

'''
def sentry_monitor(func):
    # sentry 监控
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            client.captureException()
            # client.captureMessage('Something went fundamentally wrong')
    return inner


'''
class retry(object):
    '''
    @retry(sec)
    函数执行异常时会等待sec后再重新执行一次
    适合处理访问外部资源不稳定类异常，例如数据库操作，接口访问等
    '''

    def __init__(self,sec = 1):
        self.sec = sec
    def __call__(self,function):
        def __retry(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except:
                time.sleep(self.sec)
                print('retry to run ' + function.__name__)
                result = function(*args, **kwargs)
            return result
        return __retry
    
    


    
        