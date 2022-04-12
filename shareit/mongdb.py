from pymongo import MongoClient


label_samples_col = MongoClient('127.0.0.1',27017).short_video_label.label_samples

unsupervised_sample_col = MongoClient('127.0.0.1',27017).short_video_label.unsupervised_sample


porn_sample_col = MongoClient('127.0.0.1',27017).porn.porn_sample


device_fingerprinting_sample = MongoClient('127.0.0.1',27017).disk.device_fingerprinting_sample
device_fingerprinting_sample_imei = MongoClient('127.0.0.1',27017).risk.device_fingerprinting_sample_imei
device_fingerprinting_sample_imei_all = MongoClient('127.0.0.1',27017).risk.device_fingerprinting_sample_imei_all
risk_db =  MongoClient('127.0.0.1',27017).risk

