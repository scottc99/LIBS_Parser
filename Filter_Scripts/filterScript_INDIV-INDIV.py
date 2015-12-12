import numpy as np
import glob, os, sys
import json
import re
import csv
import codecs 
import xlrd, xlwt
import operator
from xlrd import open_workbook

class LIBS_Filter_Testing: 
	
	def __init__(self):
		x = 'this still sucks!'

		self.find_fileName()

	def load_INDIV_JSON_files(self, fileName):
		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_JSON/%s/*.json'%(os.getcwd(), fileName)):
			fileName_long = file.split("/")[-1].split(".")[0]
			with codecs.open(file) as init_data_file:    
				init_json_list = json.load(init_data_file)

			self.fileName_long_list.append(fileName_long)
			self.init_json_set.append(init_json_list)

	def load_INDIV_MIN_files(self, fileName):
		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_INDIV_jsonFiles/%s/*.json'%(os.getcwd(), fileName)):
			with codecs.open(file) as min_data_file:    
				min_json_list = json.load(min_data_file)

			self.min_json_set.append(min_json_list)

	def diff_INDIV_MIN(self, fileName): 
		for x in range(len(self.init_json_set)):
			X = self.init_json_set[x]
			Y = self.min_json_set[x]

			diff_list = map(operator.sub, X, Y)

			with open('%s/Jesse_Files/filteredData_INDIV-INDIV/%s/%s.json'%(os.getcwd(), fileName, self.fileName_long_list[x]), 'w') as r:
				r.write(json.dumps(diff_list, sort_keys=True, indent=4, separators=(',', ': ')))


	def find_fileName(self):
		self.folder_name_list = []
		for file in glob.glob("%s/Jesse_Files/Testing Set-Jesse_JSON/*"%os.getcwd()):
			fileName = file.split("/")[-1]

			self.init_json_set = []
			self.min_json_set = []
			self.fileName_long_list = []

			if os.path.exists('%s/Jesse_Files/filteredData_INDIV-INDIV/%s'%(os.getcwd(), fileName)) == False:
				os.makedirs('%s/Jesse_Files/filteredData_INDIV-INDIV/%s'%(os.getcwd(), fileName))

			self.folder_name_list.append(fileName)
			
			self.load_INDIV_JSON_files(fileName)
			self.load_INDIV_MIN_files(fileName)
			self.diff_INDIV_MIN(fileName)

		print 'done filtering %s'%fileName


if __name__ == '__main__': 

	whatIsPLS = LIBS_Filter_Testing()
	whatIsPLS



