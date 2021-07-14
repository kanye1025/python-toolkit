import  pymongo
from tqdm import tqdm

def mongo_progress_bar_iterator(collection,query,filter = None,desc = None):
    total = collection.count(query)
    return tqdm(collection.find(query,filter,batch_size=5),desc =desc,total = total)