import numpy as np
import glob, os, sys
import json
import re
import csv
import codecs 
import xlrd, xlwt
from xlrd import open_workbook

class LIBS_Analyse:

	def __init__(self):
		x = 'I have all of the instance'

		self.refWavelength = []

		self.find_fileName()


	def load_controlData2(self, fileName):
		index = 0

		print 'start loading data individually...'
		for file in glob.glob("%s/Jesse_Files/Testing Set-Jesse_JSON/%s/*.json"%(os.getcwd(), fileName)):
			self.fileName_long = file.split("/")[-1].split(".")[0]
			with codecs.open(file) as json_data_file:    
				json_list = json.load(json_data_file)

			self.find_extreme_vals_INDIV(fileName, json_list)

	def find_extreme_vals_INDIV(self, fileName, json_list): 
		
		intense_min_list1 = []
		intense_min_list2 = []

		x1 = 0
		while True: 
			try: 
				if json_list[x1] > json_list[x1 - 1] and json_list[x1] > json_list[x1 + 1]:
					intense_min_list1.append(0)
				elif json_list[x1] < 0:
					intense_min_list1.append(0)
				elif json_list[x1] < json_list[x1 - 1] and json_list[x1] < json_list[x1 + 1]:
					intense_min_list1.append(json_list[x1])
					# self.avg_height_list1.append(json_list[x1])
				else: 
					intense_min_list1.append(json_list[x1])
				
				x1 += 1
			except:
				break

		intense_min_list1.append(json_list[0])
		
		# json_median = np.median(json_list)
		json_mean = np.mean(json_list)
		json_std_dev = np.std(json_list)

		# list1_median = np.median(intense_min_list1)
		list1_mean = np.mean(intense_min_list1)
		list1_std_dev = np.std(intense_min_list1)

		x2 = 0
		while True: 
			try: 
				value1 = intense_min_list1[x2]
				value1Plus = intense_min_list1[x2 + 1]
				value1Minus = intense_min_list1[x2 - 1]

				list2 = intense_min_list2

				if value1 > (list1_mean*2.5): 
					list2.append(0)
				else: 
					list2.append(value1)

				x2 += 1
			except:
				break

		intense_min_list2.append(json_list[0])		

		with open('%s/Jesse_Files/Testing Set-Jesse_INDIV_jsonFiles/%s/Min_%s.json'%(os.getcwd(), fileName, self.fileName_long), 'w') as i2:
			i2.write(json.dumps(intense_min_list2, sort_keys=True, indent=4, separators=(',', ': ')))

		with open('%s/Jesse_Files/Testing Set-Jesse_INDIV_csvFiles/%s/Min_%s.csv'%(os.getcwd(), fileName, self.fileName_long), 'w') as c2:
			writer = csv.writer(c2)
			writer.writerow(intense_min_list2)

	def find_fileName(self):
		self.folder_name_list = []
		for file in glob.glob("%s/Jesse_Files/Testing Set-Jesse_JSON/*"%os.getcwd()):
			fileName = file.split("/")[-1]

			self.folder_name_list.append(fileName)
			print fileName

			if os.path.exists('%s/Jesse_Files/Testing Set-Jesse_INDIV_jsonFiles/%s'%(os.getcwd(), fileName)) == False:
				os.makedirs('%s/Jesse_Files/Testing Set-Jesse_INDIV_jsonFiles/%s'%(os.getcwd(), fileName))

			if os.path.exists('%s/Jesse_Files/Testing Set-Jesse_INDIV_csvFiles/%s'%(os.getcwd(), fileName)) == False:
				os.makedirs('%s/Jesse_Files/Testing Set-Jesse_INDIV_csvFiles/%s'%(os.getcwd(), fileName))

			self.intensity_group = []
			self.avgIntensity_list = []

			self.load_controlData2(fileName)
		'done %s'%fileName
				

if __name__ == '__main__':
	
	itsMorphinTime = LIBS_Analyse()
	itsMorphinTime







