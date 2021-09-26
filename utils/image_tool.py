#from ..utils.os_tool import list_dir_extend,list_dir_all_files
import os

from .os_tool import list_dir_extend,list_dir_all_files


from PIL import Image

image_exts = ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif', '.tiff', '.webp']
image_exts.extend(list(map(lambda x:x.upper(),image_exts)))
image_exts = set(image_exts)
Image.MAX_IMAGE_PIXELS = 2300000000
def resize(src_image_path, dest_image_path,size):
    try:
        img = Image.open(src_image_path)
        img = img.resize(size, Image.ANTIALIAS)
        img.save(dest_image_path)
    except Exception as e:
        print(e)
        
        
        



   
    
    