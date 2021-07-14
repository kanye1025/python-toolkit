# coding=utf-8
import sys
import time
import traceback
import os
import datetime
sys.path.append(os.getcwd())
from utils.send_wx import send_wx



class Tail():
    def __init__(self,log_dir,name_list):
        self.log_dir = log_dir
        self.name_list = name_list
        self.file_name_list = self.get_files_name()
        print(self.file_name_list)
        self.files = self.get_files()


    def follow(self, n=10):
        try:
            i = 0
            while True:
                if i == 10:
                    self.remove_same_file()
                    self.change_file_count()
                    i=0
                i +=1
                start_time=datetime.datetime.now()
                for name in self.file_name_list:
                    line = self.files[name].readline()
                    line = line.strip("\n")
                    if line:
                        line = line.lower()
                        if line.count("error") > 0 or line.count("except") > 0 or line.count("rror") > 0 or line.count("xcept") > 0 or line.count("traceback"):
                            print("into")
                            line_list=[]
                            line_list.append(line)
                            for i in range(n):
                                line = self.files[name].readline()
                                line = line.strip("\n")
                                line_list.append(line)
                            print(line_list)
                            last_lines = ";".join(line_list)
                            last_infos = name + ";" + last_lines
                            send_wx(last_infos, self.name_list)
                            print(last_infos)
                time.sleep(1)
                end_time =datetime.datetime.now()
                seconds_time=(end_time-start_time).total_seconds()
                # print("all file one time use time {}".format(seconds_time))
        except Exception as err:
            print('realtime warn error {}'.format(sys.exc_info()))
            print(err)
            traceback.print_exc()

    def get_files(self):
        file_map = {}
        for name in self.file_name_list:
            f_name = open(name,"r")
            f_name.seek(0, 2)
            if name not in file_map:
                file_map[name] = f_name
        return file_map

    def get_files_name(self):
        file_name_list = []
        for dirpath, dirnames, filenames in os.walk(self.log_dir):
            for filename in filenames:
                if filename.endswith(".tmp"):
                    continue
                file_name_list.append(os.path.join(dirpath, filename))
        return file_name_list

    def remove_same_file(self):
        """
        删除生成的.1的文件
        :return:
        """
        remove_flage=False
        current_file_name = self.get_files_name()
        for name in current_file_name:
            match_obj=name.endswith(".1")
            # pattern =re.compile(r'..1')
            # match_obj = re.findall(pattern, name)
            if match_obj:
                remove_flage = True
                tmp=name + ".tmp"
                if os.path.exists(tmp):
                    os.remove(tmp)
                os.rename(name, tmp)
                new_name = name[0:len(name) - 2]
                self.files[new_name].close()
                f_name = open(new_name)
                f_name.seek(0, 2)
                self.files[new_name] = f_name
        if remove_flage:
            self.file_name_list = self.get_files_name()

    def change_file_count(self):
        """
        文件变化时，及时打开和关闭变化的文件
        :return:
        """
        current_file_name = self.get_files_name()
        current_file_count = len(current_file_name)
        file_count = len(self.file_name_list)

        if file_count != current_file_count:
            file_name_set = set(self.file_name_list)
            current_file_name_set = set(current_file_name)
            if file_count > current_file_count:
                subtract_list = file_name_set.difference(current_file_name_set)
                for ele in subtract_list:
                    self.files[ele].close()
            else:
                add_list = current_file_name_set.difference(file_name_set)
                for ele in add_list:
                    f_name = open(ele)
                    f_name.seek(0, 2)
                    self.files[ele] = f_name
            self.file_name_list = self.get_files_name()


if __name__ == '__main__':
    logdir = sys.argv[1]
    send_name = sys.argv[2]
    name_list=send_name.split(",")
    print("logdir", logdir)
    print("send_name",send_name)

    py_tail = Tail(logdir,name_list)
    py_tail.follow()
