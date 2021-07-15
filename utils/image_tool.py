from ..utils.os_tool import list_dir_extend
import os
from PIL import Image
def resize(src_image_path, dest_image_path,size):
    try:
        img = Image.open(src_image_path)
        img = img.resize(size, Image.ANTIALIAS)
        img.save(dest_image_path)
    except Exception as e:
        print(e)
        
        
        
def check_and_del_image_dir(image_dir):
    for _,file_path in list_dir_extend(image_dir):
        try:
            im = Image.open(file_path)
            #im.resize((10,10))
            if not im:
                raise Exception('cannot open image_file')
        except Exception as e:
            print(e)
            print(f'delete image file {file_path}')
            os.remove(file_path)
            
            
if __name__ == '__main__':
    check_and_del_image_dir('/datassd/kanye/face_rec/images_test_befor_online')