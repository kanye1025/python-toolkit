import urllib.request
import json
from .decorator import retry

@retry(3)
def get_data_from_json_url(url):
	response= urllib.request.urlopen(url)
	data = response.read().decode('utf-8')
	obj = json.loads(data)
	return obj