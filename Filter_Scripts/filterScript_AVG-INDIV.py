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

	def load_INDIV_JSON_files(self, fileName):
		with codecs.open('%s/Jesse_Files/Testing Set-Jesse_AVG/%s/%s.json'%(os.getcwd(), fileName, fileName)) as json_data_file:    
			avg_json_list = json.load(json_data_file)
		print len(avg_json_list)

		print 'start loading data...'
		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_INDIV_jsonFiles/%s/*.json'%(os.getcwd(), fileName)):
			self.fileName_long = file.split("/")[-1].split(".")[0].split('Min_')[-1]
			# print 'load file %s'%self.file_name
			with codecs.open(file) as json_data_file:    
				min_json_list = json.load(json_data_file)

			self.corrected_list = []
			for val in range(len(min_json_list)):
				avg_val = avg_json_list[val]
				min_val = min_json_list[val]
				
				diff = avg_val - min_val
			
				self.corrected_list.append(diff)

			with open('%s/Jesse_Files/filteredData_AVG-INDIV/%s/%s.json'%(os.getcwd(), fileName, self.fileName_long), 'w') as r:
					r.write(json.dumps(self.corrected_list, sort_keys=True, indent=4, separators=(',', ': ')))
		
	# def correct_data(self, fileName):
	# 	self.corrected_list = []
	# 	for val in range(len(self.intensity_list)):
	# 		corr_val = avg_json_list[val]
	# 		true_val = self.intensity_list[val]
			
	# 		diff = true_val - corr_val
		
	# 		self.corrected_list.append(float(diff))

	# 	with open('%s/filteredData_INDIV-AVG/%s/%s'%(os.getcwd(), fileName, self.fileName_long), 'w') as r:
	# 			r.write(json.dumps(self.corrected_list, sort_keys=True, indent=4, separators=(',', ': ')))

	def find_fileName(self):
		self.folder_name_list = []
		for file in glob.glob("%s/Jesse_Files/Testing Set-Jesse_JSON//*"%os.getcwd()):
			fileName = file.split("/")[-1]

			if os.path.exists('%s/Jesse_Files/filteredData_AVG-INDIV/%s'%(os.getcwd(), fileName)) == False:
				os.makedirs('%s/Jesse_Files/filteredData_AVG-INDIV/%s'%(os.getcwd(), fileName))

			self.folder_name_list.append(fileName)
			self.load_INDIV_JSON_files(fileName)

		print 'done filtering %s'%fileName

if __name__ == '__main__': 

	whatIsPLS = LIBS_Filter_Testing()
	whatIsPLS