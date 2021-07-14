# 通用工具代码库

#### **内存缓存**
[cached装饰器](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/cached.py)
,缓存函数返回结果，一定时间内不重新计算

[compute_tools](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/compute_tools.py)
计算工具函数：

    保留小数点后几位：exact_round
    以下三个函数适合处理以dict为行（dict-key 为field-name/col-name,dict-value 为 field-value/item-value）
    以list或其他iterable对象为列的tabel（关系数据库常用表示，iterable（dict）或list(dict)），并对其进行聚合
        对字典数组的某一列求和：sum_dict_list
        返回字典数组中某一列的最大值：max_dict_list
        返回字典数组中某一列的最大值：min_dict_list
    半衰期计算：half_life

[os_tool](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/os_tool.py)
操作系统函数

    确保文件夹存在：make_sure_dir
    
[Struct](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/pystruct.py)
一个支持直接使用属性访问field语法糖(.属性)的dict，支持多级访问。

[send_ws](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/send_wx.py)
发送企业微信消息，主要用于企业微信报警

[Time_trace](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/time_trace.py)
代码执行时间追踪，用于追踪和打印代码段的执行时间

[FileConf](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/file_conf.py)
一个读写配置文件的类，可以使用属性(.)访问配置文件下的section和key，并直接取值和赋值


[torndb](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/torndb.py)
tornado框架中的数据库读写类，解决了torndb官方代码中的一些bug

[decorator](http://git.hundun.cn/algorithm_1/toolkit/blob/master/utils/decorator.py)
一些装饰器的集合
    
    延迟加载：lazy_property
    打印函数执行时长：calc_duration
    函数异常时重新执行：retry
    
