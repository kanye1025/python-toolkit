from sklearn.metrics import classification_report

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
		