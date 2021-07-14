import xlrd
from tqdm import tqdm
from collections import Iterable


def ite_rd_pages(book_path= None,book = None):
	if not book and not book_path:
		raise Exception('book_path and book must not be None at least one')
	if not book:
		book = xlrd.open_workbook(book_path)
	for index,sheet in enumerate(book.sheets()):
		yield index,sheet.name,sheet
	
def ite_rd_page_by_index(page,col_indexes= None,skip_first_row = False):
	begin = 1 if skip_first_row else 0
	if isinstance(col_indexes,Iterable ):
		for row in tqdm(range(begin,page.nrows),desc = page.name):
			yield row,[page.cell(row,col).value for col in col_indexes]
	elif isinstance(col_indexes,int):
		for row in tqdm(range(begin,page.nrows),desc = page.name):
			yield row,page.cell(row,col_indexes).value
	elif not col_indexes:
		for row in tqdm(range(begin,page.nrows),desc = page.name):
			yield row,[page.cell(row,col).value for col in range(page.ncols)]
	else:
		raise Exception('col_indexes must be Iterable,int,or None')
	

def ite_rd_page_by_names(page,names):
	name_index = {}
	for col in range(page.ncols):
		name = page.cell(0,col).value
		name_index[name] = col
	if isinstance(names, Iterable):
		indexes = [name_index[name]for name in names]
	elif isinstance(names, str):
		indexes = name_index[names]
	else:
		raise Exception('names must be Iterable or str')
	
	
		
	
	return ite_rd_page_by_index(page,indexes,skip_first_row = True)
		
def load_page_to_dict_by_names(page,names,key):
	ret = {}
	
	for i,cols in ite_rd_page_by_names(page,names):
		obj = {}
		for name,col in zip(names,cols):
			obj[name] = col
		ret[obj[key]] = obj
	return ret
