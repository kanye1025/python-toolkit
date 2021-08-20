#from ..utils.os_tool import list_dir_extend,list_dir_all_files
from toolkit.utils.os_tool import list_dir_extend,list_dir_all_files
import os
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
        
        
        
def check_and_del_image_dir(image_dir):
    count = 0
    for _,file_path in list_dir_all_files(image_dir,matching = image_exts,rate_progress=True):
        try:
            im = Image.open(file_path)#.convert('RGB')
            im.resize((10,10)).convert('RGB')
            if not im:
                raise Exception('cannot open image_file')
        except Exception as e:
            print(e)
            print(f'delete image file {file_path}')
            os.remove(file_path)
            count+=1
    print(f'remove {count} images')

            
if __name__ == '__main__':
   
    
    check_and_del_image_dir('/data/porn/')