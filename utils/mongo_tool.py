import pymongo
from tqdm import tqdm


def mongo_progress_bar_iterator(collection, query, filter=None, desc=None, limit=None):
	total = collection.count(query)
	finder = collection.find(query, filter, batch_size=5)
	if limit:
		finder = finder.limit(limit)
	if not desc:
		desc = collection.name
	return tqdm(finder, desc=desc, total=total)
