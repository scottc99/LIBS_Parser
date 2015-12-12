import glob, os
import xlrd, xlwt
from xlrd import open_workbook
from collections import OrderedDict
import json 
import pprint


# os.chdir(os.path.dirname(os.getcwd()))
# print os.getcwd()

if __name__ == '__main__':

	for file in glob.glob("controlData_EXCEL_Files/*/*.xlsx"):
		file_folder = file.split("/")[-2]
		file_name = file.split("/")[-1]
		file_path = 'controlData_EXCEL_Files/%s/%s'%(file_folder, file_name)

		sequence1_excel = file_name.split(".")[0]
		sequence2_excel = sequence1_excel.split(" Sam")

		wb = xlrd.open_workbook(filename = file_path)
		sh = wb.sheet_by_index(0)

		LIBS_Data = {"dataset":file_path.split("/")[-1]}

		LIBS_Header = {}
		LIBS_Content = []

		#### 6/28/2015 Discussing what the header should contain ####

		LIBS_Header['Start Wavelength'] = {}
		LIBS_Header['Start Wavelength']['value'] = sh.cell_value(0, 1)
		LIBS_Header['Start Wavelength']['unit'] = 'nanometers (nm)'

		LIBS_Header['End Wavelength'] = {}
		LIBS_Header['End Wavelength']['value'] = sh.cell_value(1, 1)
		LIBS_Header['End Wavelength']['unit'] = 'nanometers (nm)'

		LIBS_Header['Gate Delay'] = {}
		LIBS_Header['Gate Delay']['value'] = sh.cell_value(2, 1)
		LIBS_Header['Gate Delay']['unit'] = 'seconds (s)'

		LIBS_Header['Gate Width'] = {}
		LIBS_Header['Gate Width']['value'] = sh.cell_value(3, 1)
		LIBS_Header['Gate Width']['unit'] = 'ms'

		LIBS_Header['Laser Output Level'] = {}
		LIBS_Header['Laser Output Level']['value'] = sh.cell_value(4, 1)
		LIBS_Header['Laser Output Level']['unit'] = ''

		LIBS_Header['X position'] = {}
		LIBS_Header['X position']['value'] = sh.cell_value(5, 1)
		LIBS_Header['X position']['unit'] = ''

		LIBS_Header['Y position'] = {}
		LIBS_Header['Y position']['value'] = sh.cell_value(6, 1)
		LIBS_Header['Y position']['unit'] = ''

		LIBS_Header['Z position'] = {}
		LIBS_Header['Z position']['value'] = sh.cell_value(7, 1)
		LIBS_Header['Z position']['unit'] = ''

		LIBS_Header['Grid Point Number'] = {}
		LIBS_Header['Grid Point Number']['value'] = sh.cell_value(8, 1)
		LIBS_Header['Grid Point Number']['unit'] = ''

		LIBS_Header['Shot Number'] = {}
		LIBS_Header['Shot Number']['value'] = sh.cell_value(9, 1)
		LIBS_Header['Shot Number']['unit'] = ''

		#### Content ####

		LIBS_Content = []

		begin = 10
		while True: 
			try: 
				row = {}

				row['wavelength'] = sh.cell_value(begin, 0)
				row['intensity'] = sh.cell_value(begin, 1)

				LIBS_Content.append(row)

				begin += 1 

			except: 
				break

		LIBS_Data['Content'] = LIBS_Content

		new_json_path = '%s/controlData_JSON_Files_fullDict/%s'%(os.getcwd(), file_folder) 
		if not os.path.exists(new_json_path): 
			os.makedirs(new_json_path)

		with open('%s/%s.json'%(new_json_path, sequence1_excel), 'w') as f:
			f.write(json.dumps(LIBS_Data, sort_keys=True, indent=4, separators=(',', ': ')))

	print "done"



