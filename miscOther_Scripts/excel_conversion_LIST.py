import glob, os
import xlrd, xlwt
from xlrd import open_workbook
from collections import OrderedDict
import json 
import pprint


# os.chdir(os.path.dirname(os.getcwd()))
# print os.getcwd()

if __name__ == '__main__':

	for file in glob.glob("Jesse_Files/Testing Set-Jesse_EXCEL/*/*.xlsx"):
		file_folder = file.split("/")[-2]
		file_name = file.split("/")[-1]
		file_path = 'Jesse_Files/Testing Set-Jesse_EXCEL/%s/%s'%(file_folder, file_name)

		sequence1_excel = file_name.split(".")[0]
		sequence2_excel = sequence1_excel.split(" Sam")

		wb = xlrd.open_workbook(filename = file_path)
		sh = wb.sheet_by_index(0)

		LIBS_Content = []

		begin = 10
		while True: 
			try: 
				intenseVal = sh.cell_value(begin, 1)

				LIBS_Content.append(float(intenseVal))

				begin += 1 

			except: 
				break

		new_json_path = '%s/Jesse_Files/Testing Set-Jesse_JSON/%s'%(os.getcwd(), file_folder) 
		if not os.path.exists(new_json_path): 
			os.makedirs(new_json_path)

		with open('%s/%s.json'%(new_json_path, sequence1_excel), 'w') as f:
			f.write(json.dumps(LIBS_Content, sort_keys=True, indent=4, separators=(',', ': ')))

	print "done"



