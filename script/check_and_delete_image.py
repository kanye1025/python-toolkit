import sys
import os
sys.path.append(os.getcwd())
from toolkit.utils.os_tool import list_dir_all_files
from toolkit.utils.image_tool import image_exts
from PIL import Image
from multiprocessing import Pool
import multiprocessing
total = 0
i=multiprocessing.Value("d",0)
count = multiprocessing.Value("d",0)
def proc(file_path):
    global total,i,count
    i.value +=1
    if i.value%100 == 0:
        print(f'{i.value}/{total}')
    try:
        im = Image.open(file_path)  # .convert('RGB')
        im.resize((10, 10)).convert('RGB')
        if not im:
            raise Exception('cannot open image_file')
    except Exception as e:
        print(e)
        print(f'delete image file {file_path}')
        os.remove(file_path)
        count.value += 1
        
file_paths = [file_path for _,file_path in list_dir_all_files('/data/kanye/data/logo_rec/short_video_0913',matching = image_exts,rate_progress=True)]
total = len(file_paths)
pool = Pool(128)
pool.map(proc,file_paths)
print(f'remove {count.value} images')
