#! /Users/ford_scott/anaconda/lib/python2.7/site-packages

import numpy as np
import glob, os, sys
import json 
import json as simplejson
import re
import csv
import codecs 
import xlrd, xlwt
from xlrd import open_workbook

sys.path.append("/Users/ford_scott/anaconda/envs/LIBS_dev/lib/python2.7/site-packages/PartialLeastSquares-1.0.1")
import PartialLeastSquares as PLS

np.seterr(divide='ignore', invalid='ignore')

class LIBS_Analyse:

	def __init__(self):
		x = 'I have all of the instance'

		self.refWavelength = []

		self.load_XRF_data()
		self.find_refWavelength()
		self.find_fileName()
		# self.PLS_function()

	def align(self, dataX, dataXY, reverse=False):
		if reverse:
			self.aligned = list(reversed(np.interp(list(reversed(dataX)), list(reversed(dataXY[0])), list(reversed(dataXY[1])))))
		else:
			self.aligned = list(np.interp(dataX, dataXY[0], dataXY[1]))
		
		return self.aligned

	def diff(self, dataY1, dataY2):
		dataSub = np.array(dataY1) - np.array(dataY2)
		return [abs(data) for data in list(dataSub)]

	def find_refWavelength(self):
		with codecs.open('%s/masterWavelength.json'%os.getcwd()) as listX_file:    
			wave_list = json.load(listX_file)

		self.refWavelength = wave_list

	def load_controlData(self, fileName):
		index = 0
		self.intensity_group = []
		self.avgIntensity_list = []

		print 'start loading data...'
		for file in glob.glob("%s/Jesse_Files/Testing Set-Jesse_JSON/%s/*.json"%(os.getcwd(), fileName)):
			self.file_name = file.split("/")[-1].split(".")[0]
			self.file_folder_split = self.file_name.split("_Sam")[0].split("_")[1:]
			self.file_folder = ' '.join(self.file_folder_split)
			# print 'load file %s'%self.file_name
			with codecs.open(file) as json_data_file:    
				json_list = simplejson.load(json_data_file)

			self.intensity_group.append(json_list)
		# print len(self.intensity_group)
		
		self.average_controlData(fileName)

	# def nonZeroPulse(self):

	def average_controlData(self, fileName):
		for pos in range((len(self.intensity_group[0]))):
			intensitySum_list = []
			intensityVar_list = []
			
			for index in range((len(self.intensity_group))): 
				num = self.intensity_group[index][pos]
				intensitySum_list.append(num)

			intensityAvg = sum(intensitySum_list)/len(intensitySum_list)
			self.avgIntensity_list.append(intensityAvg)
		# print len(self.intensity_group)
		
		if os.path.exists('%s/Jesse_Files/Testing Set-Jesse_AVG/%s'%(os.getcwd(), fileName)) == False:
			os.makedirs('%s/Jesse_Files/Testing Set-Jesse_AVG/%s'%(os.getcwd(), fileName))

		with open('%s/Jesse_Files/Testing Set-Jesse_AVG/%s/%s.json'%(os.getcwd(), fileName, fileName), 'w') as f:
			f.write(json.dumps(self.avgIntensity_list, sort_keys=True, indent=4, separators=(',', ': ')))

		# fileName = '%s_%s_%s_plot'%(self.sequence2, self.sequence3, self.sequence4)
		# plot.plots(self.refWavelength, self.avgIntensity, fileName)
		# self.findMaxVals(self.avgIntensity)

	def load_XRF_data(self):
		file = '%s/XRF_Training_Set.xlsx'%os.getcwd()

		wb = xlrd.open_workbook(filename = 'XRF_Training_Set.xlsx')
		sh = wb.sheet_by_index(0)

		row_index = 1
		while True: 
			try:
				XRF_data_list = []
				column_index = 1

				while True: 
					try: 
						XRF_data_list.append(sh.cell_value(row_index, column_index))

						column_index += 1
					except: 
						break 

				with open('%s/controlData_AVG_Files/%s Ref Data/XRF_%s.json'%(os.getcwd(), sh.cell_value(row_index, 0), sh.cell_value(row_index, 0)), 'w') as j:
					j.write(json.dumps(XRF_data_list, sort_keys=True, indent=4, separators=(',', ': ')))

				with open('%s/controlData_AVG_Files/%s Ref Data/XRF_%s.csv'%(os.getcwd(), sh.cell_value(row_index, 0), sh.cell_value(row_index, 0)), 'w') as c:
					writer = csv.writer(c)
					writer.writerow(XRF_data_list)

				row_index += 1
				self.XRF_listLength = len(XRF_data_list)

			except:
				break

	def find_extreme_vals(self, fileName): 
		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_AVG/%s/%s.json'%(os.getcwd(), fileName, fileName)): 
			self.sample_name = ' '.join(file.split('/')[-1].split(' Ref')[0])
			self.file_folder = file.split('/')[-2]
			
			intense_max_list = []
			intense_min_list1 = []
			intense_min_list2 = []
			wave_max_index_list = []
			wave_min_index_list = []
			wavelength_maxVals_list = []
			wavelength_minVals_list = []

			# Finding max values from 1 to 20 and finding min values in 
			# entire spectral range

			with codecs.open(file) as json_data_file:    
				json_list = json.load(json_data_file)
			# print len(json_list)
			# Start parsing through main json file to find max valuee 
			# and index wavelengths 
			self.avg_height_list1 = []
			self.avg_height_list2 = []

			x1 = 0
			while True: 
				try: 
					if json_list[x1] > json_list[x1 - 1] and json_list[x1] > json_list[x1 + 1]:
						intense_max_list.append(json_list[x1])
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
			
			# print 'Min list median: %s'%list1_median
			# print 'Original list median: %s'%json_median
			# print '###################################'
			# print 'Min list mean: %s'%list1_mean
			# print 'Original list mean: %s'%json_mean
			# print '###################################'
			# print 'Min list std_dev: %s'%list1_std_dev
			# print 'Original list std_dev: %s'%json_std_dev


			x2 = 0
			while True: 
				try: 
					value1 = intense_min_list1[x2]
					value1Plus = intense_min_list1[x2 + 1]
					value1Minus = intense_min_list1[x2 - 1]

					list2 = intense_min_list2

					# if value1Plus > 0 and value1Minus > 0 and value1 > 0:
					# 	if value1 > value1Plus and value1 > value1Minus:
					# 		list2.append(0)
					# 	else:
					# 		list2.append(value1)
					if value1 > (list1_mean*2.5): 
						list2.append(0)
					else: 
						list2.append(value1)

					x2 += 1
				except:
					break

			intense_min_list2.append(json_list[0])		

			print max(intense_min_list1)
			print max(intense_min_list2)
			# print len(intense_min_list2)

			intense_max_list.sort(reverse = True)
			del intense_max_list[self.XRF_listLength:]
			del wavelength_maxVals_list[self.XRF_listLength:]

			for x in intense_max_list: 
				wave_max_index_list.append(json_list.index(x))

			# for y in intense_min_list: 
			# 	wave_min_index_list.append(json_list.index(y))			

			for val1 in wave_max_index_list: 
				wavelength_maxVals_list.append(self.refWavelength[val1])

			# for val2 in wave_min_index_list: 
			# 	wavelength_minVals_list.append(self.refWavelength[val2])

			print 'done max and min value list'

		# Save max values to json files 

		# with open('%s/Testing Set-Jesse/%s/refWavelength.json'%(os.getcwd(), fileName), 'w') as r:
		# 	r.write(json.dumps(self.refWavelength, sort_keys=True, indent=4, separators=(',', ': ')))

		# with open('%s/Testing Set-Jesse/%s/Max_%s.json'%(os.getcwd(), fileName, fileName), 'w') as i:
			# i.write(json.dumps(intense_max_list, sort_keys=True, indent=4, separators=(',', ': ')))

		with open('%s/Jesse_Files/Testing Set-Jesse/%s/Max_refWavelength_%s.json'%(os.getcwd(), fileName, fileName), 'w') as w:
			w.write(json.dumps(wavelength_maxVals_list, sort_keys=True, indent=4, separators=(',', ': ')))

		with open('%s/Jesse_Files/Testing Set-Jesse/%s/Max_%s.csv'%(os.getcwd(), fileName, fileName), 'w') as c:
			writer = csv.writer(c)
			writer.writerow(intense_max_list)

		# Save min values to json file

		with open('%s/Jesse_Files/Testing Set-Jesse_AVG/%s/Min_%s.json'%(os.getcwd(), fileName, fileName), 'w') as i2:
			i2.write(json.dumps(intense_min_list2, sort_keys=True, indent=4, separators=(',', ': ')))

		# with open('%s/controlData_AVG_Files/%s Ref Data/Min_refWavelength_%s.json'%(os.getcwd(), fileName, fileName), 'w') as w2:
			# w2.write(json.dumps(wavelength_minVals_list, sort_keys=True, indent=4, separators=(',', ': ')))

		with open('%s/Jesse_Files/Testing Set-Jesse_AVG/%s/Min_%s.csv'%(os.getcwd(), fileName, fileName), 'w') as c2:
			writer = csv.writer(c2)
			writer.writerow(intense_min_list2)


	# def PLS_function(self):
	# 	matrix_fileX = "controlData_AVG_Files/Atkinson Quartzite Ref Data/Max_Atkinson Quartzite.csv"
	# 	matrix_fileY = "controlData_AVG_Files/Atkinson Quartzite Ref Data/XRF_Atkinson Quartzite.csv"

	# 	UNDEF = 0

	# 	pls = PLS.PartialLeastSquares(XMatrix_file = matrix_fileX, YMatrix_file = matrix_fileY, epsilon = 0.000)
	# 	pls.get_XMatrix_from_csv()
	# 	pls.get_YMatrix_from_csv()
	# 	print 'done'
	# 	B = pls.PLS()

	def find_fileName(self):
		self.folder_name_list = []
		for file in glob.glob("%s/Jesse_Files/Testing Set-Jesse/*"%os.getcwd()):
			fileName = file.split("/")[-1]

			self.folder_name_list.append(fileName)
			print fileName
		# index = 0
		# while True:
		# 	try:
		# 		self.intensity_group = []
		# 		self.avgIntensity_list = []
				
		# 		self.load_controlData(self.folder_name_list[index])
		# 		self.find_extreme_vals(self.folder_name_list[index])

		# 		index += 1
		# 	except:
		# 		break

			self.intensity_group = []
			self.avgIntensity_list = []
			
			self.load_controlData(fileName)
			self.find_extreme_vals(fileName)

				

if __name__ == '__main__':
	
	itsMorphinTime = LIBS_Analyse()
	itsMorphinTime







