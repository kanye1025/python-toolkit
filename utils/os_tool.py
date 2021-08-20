# -*- coding:utf-8 -*-
import os
import shutil
from .decorator import retry
from tqdm import tqdm
import socket
socket.setdefaulttimeout(120)
'''
操作系统工具
'''
def make_sure_dir(path):
	'''
	确保存在文件夹，不存在则创建
	:param path:
	:return:
	'''
	if not os.path.exists(path):
		os.makedirs(path)
		
def remove_file(path):
	if os.path.exists(path):
		os.remove(path)
		
_download_first = True
@retry(5)
def download_file(src_url, dest_file_path, is_cover=False):
	'''
	下载文件，可控制是否覆盖源文件
	:param src_url:    要下载的url
	:param dest_file_path:   目标文件目录
	:param is_cover:   是否覆盖，默认False
	:return:
	'''
	if not is_cover and os.path.exists(dest_file_path):
		return
	global _download_first
	if _download_first:
		import socket
		import urllib
		socket.setdefaulttimeout(60)
		from urllib.request import urlretrieve
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
		urllib.request.install_opener(opener)
	
	urlretrieve(src_url, dest_file_path)
	
	
def list_dir_all_files(dir_path,matching = None,rate_progress = True):
	ite = os.walk(dir_path)
	if rate_progress:
		ite = tqdm(ite, desc=dir_path)
		
	for root, dirs, files in ite:
		for file_name in files:
			if not matching:
				yield file_name,os.path.join(root, file_name)
			elif type(matching) == str:
				if matching in file_name:
					yield file_name, os.path.join(root, file_name)
			else:
				for m in matching:
					if m in file_name:
						yield file_name, os.path.join(root, file_name)
						break
			
def list_dir_extend(dir_path,matching = None,rate_progress = True):
	'''
	
	:param dir_path:要遍历的目标文件夹
	:param matching:匹配子串
	:return: file_name,file_path
	'''
	ite = os.listdir(dir_path)
	if rate_progress:
		ite =tqdm(ite,desc=dir_path)
	
	for file_name in ite:
		if not matching:
			yield file_name,os.path.join(dir_path,file_name)
		elif type(matching) == str:
			if matching in file_name:
				yield file_name, os.path.join(dir_path, file_name)
		else:
			for m in matching:
				if m in file_name:
					yield file_name, os.path.join(dir_path, file_name)
					break

def move_files_by_prename(prename, src_path, dest_path,ext_list):
	'''
	移动目录下所有文件名前缀为name,后缀在ext_list中的文件
	:param prename: 前缀名
	:param src_path:  原文件夹
	:param dest_path:  目的文件夹
	:param ext_list:   扩展名列表
	:return:
	'''
	for ext in ext_list:
		src_file_path = os.path.join(src_path, prename + '.'+ext)
		dest_file_path = os.path.join(dest_path, prename +'.'+ ext)
		if os.path.exists(src_file_path):
			shutil.move(src_file_path, dest_file_path)
		
def lines_count(file_name):
    from itertools import (takewhile, repeat)
    buffer = 1024 * 1024
    with open(file_name) as f:
        buf_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)
    
    
def enum_lines(file_path):
	total = lines_count(file_path)
	with open(file_path,'r',encoding='utf-8') as f:
		for line in tqdm(f, desc = 'loading:' + file_path,total=total):
			yield line
    

def merge_file_by_line(merge_file_paths,dest_file_path):
	content = set()
	for merge_file in merge_file_paths:
		with open(merge_file,'r',encoding='utf-8') as f:
			for line in f:
				content.add(line)
	with open(dest_file_path,'w',encoding='utf-8') as f:
		for line in content:
			f.write(line)
	
				
			