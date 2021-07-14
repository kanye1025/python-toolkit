from .os_tool import make_sure_dir
import os


def check_and_make_sure_models(obs_dir,local_dir,version,file_list = []):
		local_ver_dir = os.path.join(local_dir, version)
		obs_ver_dir =  os.path.join(obs_dir, version)
		
		version_ok = os.path.isdir(local_ver_dir)
		if not version_ok:
			make_sure_dir(local_ver_dir)
			cmd = 'rm -r {}'.format(local_ver_dir)
			os.system(cmd)
			os.system('obsutil sync {} {}'.format(obs_ver_dir,local_ver_dir))
		if file_list:
			is_check_ok = False
			while not is_check_ok:
				is_check_ok = True
				for local_file in file_list:
					local_path = os.path.join(local_ver_dir, local_file)
					if not os.path.isfile(local_path):
						is_check_ok = False
						obs_file_path = os.path.join(obs_ver_dir, local_file)
						cmd = 'obsutil cp  -f  {} {}'.format(obs_file_path, local_path)
						os.system(cmd)
		return local_ver_dir
	
	