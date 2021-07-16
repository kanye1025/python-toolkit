from pymongo import MongoClient

mongo_col = MongoClient('127.0.0.1',27017).short_video_label.label_samples

test_mongo_col = MongoClient('127.0.0.1',27017).short_video_label.label_samples_test


label_samples_col = MongoClient('127.0.0.1',27017).short_video_label.label_samples

unsupervised_sample_col = MongoClient('127.0.0.1',27017).short_video_label.unsupervised_sample