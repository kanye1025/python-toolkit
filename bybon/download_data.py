import os
import sys
sys.path.append(os.getcwd())
import datetime

import logging
logging.basicConfig(filename='../log.txt',
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                    level=logging.INFO)

import time

def download_data(data_name,date_str = datetime.date.today().strftime("%Y-%m-%d"),ver=''):
    begin_time = datetime.datetime.now()
    file_name = f"{data_name}_{date_str}.csv"
    cmd =f"mkdir ./data{ver}/{date_str}"
    os.system(cmd)
    while True:

        cmd = f"aliyun oss cp oss://bybon-algorithm/prod/intelligent_storage{ver}/outport_datas/{date_str}/{file_name}   ./data{ver}/{date_str}/{file_name}"
        logging.info(cmd)
        os.system(cmd)
        if not os.path.exists(f"./data{ver}/{date_str}/{file_name}"):
            now = datetime.datetime.now()
            if (now-begin_time).seconds>=5*3600: #5个小时都没有获得数据，退出
                logging.error(f"{file_name} not exists")
                return False
            time.sleep(300) #没有数据，5分钟后重试
            continue
        else:
            logging.info(f"{file_name}  download ok")
            return True

