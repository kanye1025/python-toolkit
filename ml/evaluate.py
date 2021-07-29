from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import numpy as np
def get_confusion_matrix_from_xls(xls_path,true_field,pred_field,sheet_name = None,sheet_index = 0,proc_true = None,proc_pred = None):
	import xlrd
	from ..utils.xls_tools import  ite_rd_page_by_names,ite_rd_page_by_index
	book = xlrd.open_workbook(xls_path)
	if sheet_name:
		sheet = book.sheet_by_name(sheet_name)
	else:
		sheet = book.sheet_by_index(sheet_index)
	trues = []
	preds = []
	labels = set()
	if type(true_field) == str:
		ite = ite_rd_page_by_names(sheet, [true_field, pred_field])
	elif type(true_field) == int:
		ite = ite_rd_page_by_index(sheet, [true_field, pred_field], skip_first_row=True)
	for raw, (true, pred) in ite:
		if proc_true:
			true = proc_true(true)
		if proc_pred:
			pred = proc_pred(pred)
		trues.append(true)
		preds.append(pred)
		labels.add(true)
		labels.add(pred)
	labels = list(labels)
	cm = confusion_matrix(trues,preds,labels)
	label_count = len(labels)
	cm2 = []
	for i in (range(label_count+1)):
		l = []
		for j in (range(label_count+1)):
			l.append(None)
		cm2.append(l)
	for i,label in enumerate(labels):
		cm2[0][i+1] = label
		cm2[i+1][0] = label
	for i in range(label_count):
		for j in range(label_count):
			cm2[i+1][j+1] = cm[i][j]
		
	return  cm2
		

def evaluate_from_xls(xls_path,true_field,pred_field,sheet_name = None,sheet_index = 0,proc_true = None,proc_pred = None,output_dict=False,
                          zero_division=0):
	import xlrd
	from ..utils.xls_tools import  ite_rd_page_by_names,ite_rd_page_by_index
	
	book = xlrd.open_workbook(xls_path)
	if sheet_name:
		sheet = book.sheet_by_name(sheet_name)
	else:
		sheet = book.sheet_by_index(sheet_index)
	trues = []
	preds = []
	if type(true_field) == str:
		ite = ite_rd_page_by_names(sheet,[true_field,pred_field])
	elif type(true_field) == int:
		ite = ite_rd_page_by_index(sheet, [true_field, pred_field],skip_first_row = True)
	for raw ,(true,pred) in ite:
		if proc_true:
			true = proc_true(true)
		if proc_pred:
			pred = proc_pred(pred)
		trues.append(true)
		preds.append(pred)
		
	return classification_report(y_true=trues,y_pred=preds,digits = 5,output_dict = output_dict,zero_division =zero_division)
		