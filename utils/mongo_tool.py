import pymongo
from tqdm import tqdm


def mongo_progress_bar_iterator(collection, query, filter=None, sort = None, limit=None,desc=None):
	
	total = collection.count(query)
	finder = collection.find(query, filter, batch_size=5)
	if sort:
		finder = finder.sort(sort)
	if limit:
		finder = finder.limit(limit)
	if not desc:
		desc = collection.name
	return tqdm(finder, desc=desc, total=min(total,limit))
