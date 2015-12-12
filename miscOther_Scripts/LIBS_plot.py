import glob, os
from collections import OrderedDict
import json 	
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import show, plot, ion
import pylab
import numpy as np
import math
import re
import codecs
from collections import defaultdict

class LIBS_Plotting: 
	def init(self): 
		x = 'no, all of your instance are belong to us' 

		print 'init'

		self.file_name_group = {}
		self.folder_name_group = []
		
		for file in glob.glob('%s/controlData_AVG_Files/*'%os.getcwd()):
			folder_name = file.split("/")[-1]
			self.file_name_group['%s'%folder_name] = {}
			self.file_name_group['%s'%folder_name]['maxWaveNum'] = []
			self.file_name_group['%s'%folder_name]['minWaveNum'] = []
			self.file_name_group['%s'%folder_name]['xrfNum'] = []
			self.file_name_group['%s'%folder_name]['maxNum'] = []
			self.file_name_group['%s'%folder_name]['minNum'] = []
			self.file_name_group['%s'%folder_name]['refWaveNum'] = []
			self.file_name_group['%s'%folder_name]['rockNum'] = []
		
		self.loadFiles()
	
	def loadFiles(self):
		for file in glob.glob('%s/controlData_AVG_Files/*/*.json'%os.getcwd()):
			front_part = file.split("/")[-1].split('.')[0]
			file_name = file.split('/')[-1]
			folder_name = file.split("/")[-2]
			rock_name = ''.join(folder_name.split(' Ref')[0])
			self.file_name_NOjson = file.split('/')[-1].split('.')[0]
			
			if folder_name not in self.folder_name_group:
				self.folder_name_group.append(folder_name)
			elif folder_name in self.folder_name_group:
				pass

			max_part = re.search('Max_%s'%rock_name, front_part)
			min_part = re.search('Min_%s'%rock_name, front_part)
			xrf_part = re.search('XRF', front_part)
			max_wave = re.search('Max_refWavelength', front_part)
			min_wave = re.search('Min_refWavelength', front_part)
			ref_part = re.search('refWavelength', front_part)
			rock_part = re.search('%s'%rock_name, front_part)

			if max_wave:
				with codecs.open(file) as json_data_file:    
					json_list_max_wave = json.load(json_data_file)
				maxWaveNum = list(json_list_max_wave)
				
				for valMaxWaveNum in maxWaveNum:
					self.file_name_group['%s'%folder_name]['maxWaveNum'].append(valMaxWaveNum)

			elif min_wave:
				with codecs.open(file) as json_data_file:    
					json_list_min_wave = json.load(json_data_file)
				minWaveNum = list(json_list_min_wave)
				
				for valMinWaveNum in minWaveNum:
					self.file_name_group['%s'%folder_name]['minWaveNum'].append(valMinWaveNum)

			elif xrf_part:
				with codecs.open(file) as json_data_file:      
					json_list_XRF = json.load(json_data_file)
				xrfNum = list(json_list_XRF)
				
				for valxrfNum in xrfNum: 
					self.file_name_group['%s'%folder_name]['xrfNum'].append(valxrfNum)

			elif max_part:
				with open(file) as json_data_file:    
					json_list_max = json.load(json_data_file)
				maxNum = list(json_list_max)
				
				for valmaxNum in maxNum:
					self.file_name_group['%s'%folder_name]['maxNum'].append(valmaxNum)

			elif min_part:
				with open(file) as json_data_file:    
					json_list_min = json.load(json_data_file)
				minNum = list(json_list_min)
				
				for valminNum in minNum:
					self.file_name_group['%s'%folder_name]['minNum'].append(valminNum)	

			elif ref_part:
				with open(file) as json_data_file:    
					json_list_ref = json.load(json_data_file)
				refWaveNum = list(json_list_ref)
				
				for valRefWaveNum in refWaveNum:
					self.file_name_group['%s'%folder_name]['refWaveNum'].append(valRefWaveNum)	

			elif rock_part:
				with open(file) as json_data_file:    
					json_list_rock = json.load(json_data_file)
				rockNum = list(json_list_rock)
				
				for valRockNum in rockNum:
					self.file_name_group['%s'%folder_name]['rockNum'].append(valRockNum)	

			# else:
			# 	with codecs.open(file) as json_data_file:      
			# 		json_list_avg = json.load(json_data_file)
			# 	avgNum = list(json_list_avg)
				
			# 	for valavgNum in avgNum: 
			# 		self.file_name_group['%s'%folder_name]['avgNum'].append(valavgNum)
				
			self.maxWaveNum_new = [maxWaveNum for maxWaveNum in self.file_name_group['%s'%folder_name]['maxWaveNum'] if maxWaveNum != []]
			self.minWaveNum_new = [minWaveNum for minWaveNum in self.file_name_group['%s'%folder_name]['minWaveNum'] if minWaveNum != []]
			self.xrfNum_new = [xrfNum for xrfNum in self.file_name_group['%s'%folder_name]['xrfNum'] if xrfNum != []]
			self.maxNum_new = [maxNum for maxNum in self.file_name_group['%s'%folder_name]['maxNum'] if maxNum != []] 
			self.minNum_new = [minNum for minNum in self.file_name_group['%s'%folder_name]['minNum'] if minNum != []] 
			self.refWaveNum_new = [refWaveNum for refWaveNum in self.file_name_group['%s'%folder_name]['refWaveNum'] if refWaveNum != []] 
			self.rockNum_new = [rockNum for rockNum in self.file_name_group['%s'%folder_name]['rockNum'] if rockNum != []] 

		self.load_plot_data()
			# print len(self.x_new)
			# print len(self.maxNum_new)
			# print len(self.xrfNum_new)

	def load_plot_data(self):		
		self.rock_type_list = self.folder_name_group

		for x in range(len(self.rock_type_list)):
			fileName = self.rock_type_list[x]

			if os.path.exists('%s/Figures/%s'%(os.getcwd(), fileName)) == False:
				os.makedirs('%s/Figures/%s'%(os.getcwd(), fileName))
			
			maxWaveNum = self.file_name_group[self.rock_type_list[x]]['maxWaveNum']
			maxNum = self.file_name_group[self.rock_type_list[x]]['maxNum']
			xrfNum = self.file_name_group[self.rock_type_list[x]]['xrfNum']
			minWaveNum = self.file_name_group[self.rock_type_list[x]]['minWaveNum']
			minNum = self.file_name_group[self.rock_type_list[x]]['minNum']
			refWaveNum = self.file_name_group[self.rock_type_list[x]]['refWaveNum']
			rockNum = self.file_name_group[self.rock_type_list[x]]['rockNum']


			plt.plot(self.file_name_group[self.rock_type_list[x]]['maxWaveNum'],\
					   self.file_name_group[self.rock_type_list[x]]['maxNum'], 'ro', ms = 2.5, mec = 'k')
			plt.axis([min(maxWaveNum) - 20, max(maxWaveNum) + 20, min(maxNum) - abs((min(maxNum)*.25)), max(maxNum) + (max(maxNum)*.25)])
			plt.savefig('Figures/%s/Max_%s_plot'%(fileName, fileName))
			plt.close()

			plt.plot(self.file_name_group[self.rock_type_list[x]]['refWaveNum'],\
					   self.file_name_group[self.rock_type_list[x]]['minNum'], 'ro', ms = 2.5, mec = 'k')	
			plt.axis([min(minWaveNum) - 20, max(minWaveNum) + 20, min(minNum) - abs((min(minNum)*.25)), max(minNum) + (max(minNum)*.25)])
			plt.savefig('Figures/%s/Min_%s_plot'%(fileName, fileName))
			plt.close()

			plt.plot(self.file_name_group[self.rock_type_list[x]]['maxWaveNum'],\
					   self.file_name_group[self.rock_type_list[x]]['xrfNum'], 'ko', ms = .5, mec = 'k')
			plt.axis([min(maxWaveNum) - 20, max(maxWaveNum) + 20, min(xrfNum) - abs((min(xrfNum)*.25)), max(xrfNum) + (max(xrfNum)*.25)])
			plt.savefig('Figures/%s/XRF_%s_plot'%(fileName, fileName))
			plt.close()
			
			plt.plot(self.file_name_group[self.rock_type_list[x]]['refWaveNum'],\
					   self.file_name_group[self.rock_type_list[x]]['rockNum'], 'ko', ms = 2.0, mec = 'k')
			plt.plot(self.file_name_group[self.rock_type_list[x]]['refWaveNum'],\
					   self.file_name_group[self.rock_type_list[x]]['minNum'], 'ro', ms = 1.0, mec = 'r')
			plt.axis([min(refWaveNum) - 20, max(refWaveNum) + 20, min(rockNum) - abs((min(rockNum)*.25)), max(rockNum) + (max(rockNum)*.25)])
			plt.savefig('Figures/%s/comparison_%s'%(fileName, fileName))
			plt.close()


if __name__ == '__main__':
	plotGraphs = LIBS_Plotting()
	plotGraphs.init()
	print "done"



	