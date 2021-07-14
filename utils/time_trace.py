# -*- coding: utf-8 -*-


import time
import datetime

class Time_trace():
    '''
    记录和打印代码段执行时间的工具，调用show打印相邻追踪点之间的执行时间信息。
    '''
    def __init__(self,trace_name,debug = False):
        '''
        :param trace_name:  模块名
        :param debug:       是否为debug模式，默认False不打印日志
        '''
        self.debug = debug
        if debug:
            self.t = []
            self.name = trace_name
            self.trace('begin')

    def __del__(self):
        self.show()
    def trace(self,seg_name):
        '''
        设置名称为seg_name的追踪点，
        :param seg_name:
        :return:
        '''
        if self.debug:
            self.t.append((seg_name,datetime.datetime.now()))

    def show(self):
        if self.debug:
            self.trace('end')
            begin = self.t[0]
            print('time tracer:%s  total:%d'%(self.name,(self.t[-1][1]-self.t[0][1]).total_seconds()*1000000))
            n1,t1 = self.t[0]
            for n2,t2 in self.t[1:]:
                print ('between %s and %s:%d'%(n1,n2,(t2-t1).total_seconds()*1000000))
                n1,t1 = n2,t2


