from io import BytesIO
from PIL import Image
import lmdb
from toolkit.utils.url_tool import get_data_from_url
from toolkit.utils.os_tool import list_dir_extend
def donwload_image_to_lmdb(lmdb_env,url,key,resize = None,recover = False):
	if not recover:
		txn = lmdb_env.begin(write=False)
		buf = txn.get(key.encode(),None)
		if buf:
			return
		
	buf = get_data_from_url(url)
	if resize:
		img = Image.open(BytesIO(buf)).resize(resize, Image.ANTIALIAS)
		data_byte = BytesIO()
		img.save(data_byte, format='webp')
		buf = data_byte.getbuffer()
	txn = lmdb_env.begin(write=True)
	txn.put(key.encode(),buf)
	txn.commit()
	
	
def dir_to_lmdb(lmdb_env,file_dir):
	
	for file_name,file_path in list_dir_extend(file_dir):
		with open(file_path, 'br') as f :
			buf = f.read()
			if buf:
				txn = lmdb_env.begin(write=True)
				txn.put(file_name.encode(), buf)
				txn.commit()
			
		