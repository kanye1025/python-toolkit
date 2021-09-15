import sys
import os
sys.path.append(os.getcwd())
from src.toolkit.utils.os_tool import list_dir_all_files
from src.toolkit.utils.image_tool import image_exts
from PIL import Image
from multiprocessing import Pool
total = 0
i = 0
count = 0
def proc(file_path):
    global total,i,count
    i+=1
    if i%100 == 0:
        print(f'{i}/{total}')
    try:
        im = Image.open(file_path)  # .convert('RGB')
        im.resize((10, 10)).convert('RGB')
        if not im:
            raise Exception('cannot open image_file')
    except Exception as e:
        print(e)
        print(f'delete image file {file_path}')
        os.remove(file_path)
        count += 1
        
file_paths = [file_path for _,file_path in list_dir_all_files('/data/kanye/data/logo_rec/BG',matching = image_exts,rate_progress=True)]

pool = Pool(64)
pool.map(proc,file_paths)
print(f'remove {count} images')
