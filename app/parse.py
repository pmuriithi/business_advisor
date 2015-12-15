import os
import json
import xlrd
from xlrd import open_workbook
from flask import Flask

#path = 'C:\\Users\\POLY\\Google Drive\\Desktop\\UPC\\BIP\\project\\temp\\test\\'
path = "C:\\Users\POLY\\Google Drive\\Desktop\UPC\\BIP\\business_advisor\\app\\test"
filename = ''

def parse_file(filename):
	base = os.path.basename(os.path.join(path,filename))
	base_filename = (os.path.splitext(base)[0]) # print the name split without an extension
	filename_suffix = 'json'
	#split the file to filename without the path
	book = open_workbook(os.path.join(path,filename))
	sheet = book.sheet_by_index(0)
	for r in range(0,sheet.nrows): #create a list with all row numbers that contain data and loop through it
		for c in range(0, sheet.ncols):       #create a list with all column numbers that contain data and loop through i
			if sheet.cell_type(r, c) == xlrd.XL_CELL_EMPTY:
				sheet._cell_values[r][c] = 'NULL'
	# read header values into the list    
	keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]

	dict_list = []
	for row_index in range(1, sheet.nrows):
		d = {keys[col_index]: sheet.cell(row_index, col_index).value 
			for col_index in range(sheet.ncols)}
		dict_list.append(d)

	#print dict_list
	# Write to file
	with open(os.path.join(path, base_filename + "." + filename_suffix), 'w') as f:
		f.write(json.dumps(dict_list))
	return os.path.join(path, base_filename + "." + filename_suffix)
	

		