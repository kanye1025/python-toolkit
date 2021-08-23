from toolkit.utils.url_tool import get_data_from_json_url
def get_video_item_obj(item_id):
	url = f'http://prod.dc-query.sbos.sg2.api/dc-query/getItem?itemId={item_id}'
	obj = get_data_from_json_url(url)
	if 'data' in obj:
		return obj['data']
	return None

