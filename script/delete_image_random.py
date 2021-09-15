from src.toolkit.utils.os_tool import list_dir_extend
import os


file_dir = '/data/kanye/data/mini_video/videos/Status'

i = 0
for _,file_path in list_dir_extend(file_dir):
	i+=1
	if i%2==0:
		os.remove(file_path)
