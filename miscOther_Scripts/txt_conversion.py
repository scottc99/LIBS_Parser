import glob, os
import csv 
import sys
import json 
import xlrd, xlwt

if __name__ == '__main__':

	for file in glob.glob('controlData_TXT_Files/*/*.txt'):
		file_path_init = file.split(".")[0].split(" ")
		file_path = '_'.join(file_path_init)
		file_name = file_path.split("/")[-1]
		
		sequence1 = file.split("/")[-1].split(".")[0]
		sequence2 = sequence1.split(" Sam")[0].split(" ")[1:]
		sequence3 = ' '.join(sequence2)
		print file_path
		print "Converting %s to excel..."%file
		with open(file, "r") as txt_file:
			workbook = xlwt.Workbook()
			sheet = workbook.add_sheet('dataset')
 
			content = txt_file.read().split("\n")
			row_index = 0
			for row in content:
				columns = row.split()
				column_index = 0
				for column in columns:
					sheet.write(row_index, column_index, column.decode('ISO8859-1'))
					column_index += 1
				row_index += 1

			if not os.path.exists('%s/controlData_EXCEL_Files/%s'%(os.getcwd(), sequence3)):
				os.makedirs('%s/controlData_EXCEL_Files/%s'%(os.getcwd(), sequence3))
			
			workbook.save('%s/controlData_EXCEL_Files/%s/%s.xlsx'%(os.getcwd(), sequence3, file_name))