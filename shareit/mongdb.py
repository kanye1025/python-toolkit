from pymongo import MongoClient

mongo_col = MongoClient('127.0.0.1',27017).short_video_label.label_samples

test_mongo_col = MongoClient('127.0.0.1',27017).short_video_label.label_samples_test