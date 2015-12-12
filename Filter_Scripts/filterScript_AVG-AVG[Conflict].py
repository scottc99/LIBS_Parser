import numpy as np
import glob, os, sys
import json
import re
import csv
import codecs 
import xlrd, xlwt
from xlrd import open_workbook

class LIBS_Filter_Testing: 
	
	def __init__(self):
		x = 'this still sucks!'

		self.find_fileName()

	def load_AVG_JSON_file(self, fileName):
		file = '%s/Jesse_Files/Testing Set-Jesse_AVG/%s/%s.json'%(os.getcwd(), fileName, fileName)
		# self.fileName_long = file.split("/")[-1].split(".")[0]
		with codecs.open(file) as init_data_file:    
			self.init_json_list = json.load(init_data_file)

	def load_AVG_MIN_file(self, fileName):
		file = '%s/Jesse_Files/Testing Set-Jesse_AVG/%s/Min_%s.json'%(os.getcwd(), fileName, fileName)
		with codecs.open(file) as min_data_file:    
			self.min_json_list = json.load(min_data_file)

	def diff_AVG_MIN(self, fileName): 
		for val in range(len(self.init_json_list)):
			minimum = self.min_json_list[val]
			initial = self.init_json_list[val]
			
			diff = initial - minimum
		
			self.diff_list.append(diff)

	def find_fileName(self):
		self.folder_name_list = []
		for file in glob.glob("%s/Jesse_Files/Testing Set-Jesse_JSON//*"%os.getcwd()):
			fileName = file.split("/")[-1]

			if os.path.exists('%s/Jesse_Files/filteredData_AVG-AVG'%os.getcwd()) == False:
				os.makedirs('%s/Jesse_Files/filteredData_AVG-AVG'%os.getcwd())

			self.init_json_list = []
			self.min_json_list = []
			self.diff_list = []

			self.folder_name_list.append(fileName)
			self.load_AVG_JSON_file(fileName)
			self.load_AVG_MIN_file(fileName)
			self.diff_AVG_MIN(fileName)

			with open('%s/Jesse_Files/filteredData_AVG-AVG/%s_filterAVG.json'%(os.getcwd(), fileName), 'w') as r:
				r.write(json.dumps(self.diff_list, sort_keys=True, indent=4, separators=(',', ': ')))

			print 'done filtering %s'%fileName

if __name__ == '__main__': 

	whatIsPLS = LIBS_Filter_Testing()
	whatIsPLS







