import urllib.request
import json
from .decorator import retry
import requests
@retry(3)
def get_data_from_json_url(url):
	response= urllib.request.urlopen(url)
	data = response.read().decode('utf-8')
	obj = json.loads(data)
	return obj

@retry(3)
def get_data_from_url(url):
	response = requests.get(url)
	if response.status_code == requests.codes.ok:
		return response.content
	else:
		raise Exception(f'requests error code :{response.status_code}'
		                f'url :{url}')
	