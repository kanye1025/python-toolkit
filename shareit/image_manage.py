import os
import hashlib
from ..utils.os_tool import download_file
from ..utils.decorator import retry
import requests
import PIL
from PIL import Image
from io import  BytesIO
img_roots = ['/data/sample_image/all_image','/data/sample_image/all_image1']
img_root = '/data/sample_image/all_image1'

def image_exists(image_file_name):
    for ir in img_roots:
        image_path = os.path.join(ir, image_file_name)
        if  os.path.exists(image_path):
            return image_path
    return None

def gen_image_path(image_file_name):
    return os.path.join(img_root,image_file_name)


def url_md5(url):
    return hashlib.md5(url.encode('utf-8')).hexdigest()



def url_to_donwload_domain_aws_cdn(img_url):
    img_url = img_url.split('/')
    if len(img_url)>=3:
        img_url[2] = 'aws-cdn.wshareit.com'
    else:
        print(img_url)
    img_url = '/'.join(img_url)
    return img_url

def url_to_donwload_domain_s3(img_url):
    img_url = img_url.split('/')
    if len(img_url)>=3:
        img_url[2] = 's3://shareit.files.sg'
        img_url = img_url[2:]
    else:
        print(img_url)
    img_url = '/'.join(img_url)
    return img_url

@retry(3)
def download_and_resize_img(url, image_path):
    resp = requests.get(url)
    img = Image.open(BytesIO(resp.content))
    img = img.resize((250, 250), Image.ANTIALIAS)
    img.save(image_path)
    
    
@retry(3)
def download_s3(url,file_path,is_cover=False):
    if not is_cover and os.path.exists(file_path):
        return
    url = url_to_donwload_domain_s3(url)
    cmd = f'aws s3 cp {url} {file_path}'
    print(cmd)
    os.system(cmd)
    
    
@retry(3)
def download_aws_cdn(url,file_path,is_cover=False):
    url = url_to_donwload_domain_aws_cdn(url)
    download_file(url,file_path,is_cover=is_cover)



def donwload_resize_to_md5(img_url,cover = False):
    img_url = img_url
    _, ext = os.path.splitext(img_url)
    md5 = hashlib.md5(img_url.encode('utf-8')).hexdigest()
    img_url = url_to_donwload_domain_aws_cdn(img_url)
    file_name = md5 + ext
    image_path = image_exists(file_name)
    if not image_path:
        image_path = gen_image_path(file_name)
    if cover or not os.path.exists(image_path):
        try:
            download_and_resize_img(img_url, image_path)
        except Exception as e:
            print(e)
            print(img_url)
            return None,None
    return image_path,md5
    
    
        


if '__main__' == __name__:
    download_s3('http://cdn.ushareit.com/sz2/fr/original/210610/v4DaPx/frame_676.jpg','data/test676.jpg')