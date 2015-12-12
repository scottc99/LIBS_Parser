import glob, os
import json
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import show, plot, ion
from pylab import *
import numpy as np
import math
import codecs

class Filter_Plots_IND_IND: 
	def __init__(self):
		x = 'lets plot and stuff'

		self.import_masterWavelength()

	def import_masterWavelength(self): 
		file = '%s/masterWavelength.json'%os.getcwd()

		with codecs.open(file) as wave_file:
			wave_list = json.load(wave_file)
		self.refWavelength = wave_list

		self.find_fileName()

	def plot_INDIV_INDIV(self, fileName):
		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_JSON/%s/*.json'%(os.getcwd(), fileName)):
			with codecs.open(file) as json_file: 
				original_list = json.load(json_file)
			
			name = file.split('/')[-1].split('.')[0]
			self.fileName_long_list.append(name)

			self.original_set.append(original_list)

		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_INDIV_jsonFiles/%s/*.json'%(os.getcwd(), fileName)):
			with codecs.open(file) as json_file: 
				minimum_list = json.load(json_file)

			self.minimum_set.append(minimum_list)

		for file in glob.glob('%s/Jesse_Files/filteredData_INDIV-INDIV/%s/*.json'%(os.getcwd(), fileName)):
			with codecs.open(file) as json_file: 
				filtered_list = json.load(json_file)

			self.filtered_set.append(filtered_list)

		x = self.refWavelength
		orig = self.original_set
		mini = self.minimum_set 
		fill = self.filtered_set

		# print len(orig)
		# print len(mini)
		# print len(fill) 

		pos = 0 
		while True: 
			try: 
				# xmin = min(x)
				# xmax = max(x)
				# ymin = 0
				# ymax = max(orig[pos])*(.05)

				# ax = [min(x), max(x), 0, max(orig[pos]) + max(orig[pos])*(.05)]
				np.linspace(min(x), max(x), 0, max(orig[pos])*(.05))

				plt.subplot(3,1,1)
				plt.plot(x, orig[pos], 'ko', ms = 1.5, mec = 'k')
				# plt.axis(ax)
				# plt.yscale(200000)
				plt.title('Raw')
				plt.grid(True)

				plt.subplot(3,1,2)
				plt.plot(x, mini[pos], 'go', ms = 1.5, mec = 'g')
				# plt.axis(ax)
				# plt.yscale(200000)
				plt.title('Minimum')
				plt.grid(True)

				plt.subplot(3,1,3)
				plt.plot(x, fill[pos], 'bo', ms = 1.5, mec = 'b')
				# plt.axis(ax)
				# plt.yscale(200000)
				plt.title('Filtered')
				plt.grid(True)

				plt.savefig('%s/Jesse_Plots/plot_INDIV-INDIV/%s/%s_plot'%(os.getcwd(), fileName, self.fileName_long_list[pos]))
				plt.close()

				pos += 1
			except:
				break

	def find_fileName(self):
		self.folder_name_list = []
		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_JSON/*'%os.getcwd()):
			fileName = file.split("/")[-1]

			self.original_set = []
			self.minimum_set = []
			self.filtered_set = []

			self.fileName_long_list = []

			if os.path.exists('%s/Jesse_Plots/plot_INDIV-INDIV/%s'%(os.getcwd(), fileName)) == False:
				os.makedirs('%s/Jesse_Plots/plot_INDIV-INDIV/%s'%(os.getcwd(), fileName))

			self.folder_name_list.append(fileName)
			
			self.plot_INDIV_INDIV(fileName)

# class Filter_Plots_IND_AVG: 
# 	def __init__(snap):
# 		x = 'lets plot and stuff'

# 		snap.find_fileName()

# 	def import_masterWavelength(snap): 
# 		file = '%s/masterWavelength.json'%os.getcwd()
# 		with codecs.open(file) as wave_file:
# 			snap.refWavelength = json.load(wave_file)

# 	def plot_INDIV_AVG(snap, fileName):
# 		if os.path.exists('%s/Jesse_Plots/plot_INDIV-AVG'%os.getcwd()) == False:
# 			os.makedirs('%s/Jesse_Plots/plot_INDIV-AVG'%os.getcwd())

# 		for file in glob.glob('%s/Jesse_Files/filteredData_INDIV-AVG/%s/*.json'%(os.getcwd(), fileName)):
# 			with codecs.open(file) as json_file: 
# 				snap.ind_avg_list = json.load(json_file)

# 			plt.plot(snap.refWavelength, snap.ind_avg_list, 'ro', ms = 2.5, mec = 'k')
# 			plt.axis()
# 			plt.savefig('%s/Jesse_Plots/plot_INDIV-AVG/%s_plot'%(os.getcwd(), fileName))
# 			plt.close()

# 	def find_fileName(snap):
# 		snap.folder_name_list = []
# 		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_JSON/*'%os.getcwd()):
# 			fileName = file.split("/")[-1]

# 			snap.init_json_set = []
# 			snap.min_json_set = []
# 			snap.fileName_long_list = []

# 			if os.path.exists('%s/Jesse_Plots/plot_INDIV-INDIV/%s_plot'%(os.getcwd(), fileName)) == False:
# 				os.makedirs('%s/Jesse_Plots/plot_INDIV-INDIV/%s_plot'%(os.getcwd(), fileName))

# 			snap.folder_name_list.append(fileName)
			
# 			snap.load_INDIV_JSON_files(fileName)
# 			snap.load_INDIV_MIN_files(fileName)
# 			snap.diff_INDIV_MIN(fileName)

# class Filter_Plots_AVG_AVG: 
# 	def __init__(crackle):
# 		x = 'lets plot and stuff'

# 		crackle.find_fileName()

# 	def import_masterWavelength(crackle): 
# 		file = '%s/masterWavelength.json'%os.getcwd()
# 		with codecs.open(file) as wave_file:
# 			crackle.refWavelength = json.load(wave_file)

# 	def plot_AVG_INDIV(crackle, fileName): 
# 		if os.path.exists('%s/Jesse_Plots/plot_AVG-INDIV'%os.getcwd()) == False:
# 			os.makedirs('%s/Jesse_Plots/plot_AVG-INDIV'%os.getcwd())

# 		for file in glob.glob('%s/Jesse_Files/filteredData_AVG-INDIV/%s/*.json'%(os.getcwd(), fileName)):
# 			with codecs.open(file) as json_file: 
# 				crackle.avg_ind_list = json.load(json_file)

# 			plt.plot(crackle.refWavelength, crackle.avg_ind_list, 'ro', ms = 2.5, mec = 'k')
# 			plt.axis()
# 			plt.savefig('%s/Jesse_Plots/plot_AVG-INDIV/%s_plot'%(os.getcwd(), fileName))
# 			plt.close()

# 	def find_fileName(crackle):
# 		crackle.folder_name_list = []
# 		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_JSON/*'%os.getcwd()):
# 			fileName = file.split("/")[-1]

# 			crackle.init_json_set = []
# 			crackle.min_json_set = []
# 			crackle.fileName_long_list = []

# 			if os.path.exists('%s/Jesse_Plots/plot_INDIV-INDIV/%s_plot'%(os.getcwd(), fileName)) == False:
# 				os.makedirs('%s/Jesse_Plots/plot_INDIV-INDIV/%s_plot'%(os.getcwd(), fileName))

# 			crackle.folder_name_list.append(fileName)
			
# 			crackle.load_INDIV_JSON_files(fileName)
# 			crackle.load_INDIV_MIN_files(fileName)
# 			crackle.diff_INDIV_MIN(fileName)

# class Filter_Plots_AVG_IND: 
# 	def __init__(pop):
# 		x = 'lets plot and stuff'

# 		crackle.find_fileName()

# 	def import_masterWavelength(pop): 
# 		file = '%s/masterWavelength.json'%os.getcwd()
# 		with codecs.open(file) as wave_file:
# 			pop.refWavelength = json.load(wave_file)

# 	def plot_AVG_AVG(pop, fileName):
# 		if os.path.exists('%s/Jesse_Plots/plot_AVG-AVG'%os.getcwd()) == False:
# 			os.makedirs('%s/Jesse_Plots/plot_AVG-AVG'%os.getcwd())

# 		for file in glob.glob('%s/Jesse_Files/filteredData_AVG-AVG/%s/*.json'%(os.getcwd(), fileName)):
# 			with codecs.open(file) as json_file: 
# 				pop.avg_avg_list = json.load(json_file)

# 			plt.plot(pop.refWavelength, pop.avg_avg_list, 'ro', ms = 2.5, mec = 'k')
# 			plt.axis()
# 			plt.savefig('%s/Jesse_Plots/plot_AVG-AVG/%s_plot'%(os.getcwd(), fileName))
# 			plt.close()

# 	def find_fileName(pop):
# 		pop.folder_name_list = []
# 		for file in glob.glob('%s/Jesse_Files/Testing Set-Jesse_JSON/*'%os.getcwd()):
# 			fileName = file.split("/")[-1]

# 			pop.init_json_set = []
# 			pop.min_json_set = []
# 			pop.fileName_long_list = []

# 			if os.path.exists('%s/Jesse_Plots/plot_INDIV-INDIV/%s_plot'%(os.getcwd(), fileName)) == False:
# 				os.makedirs('%s/Jesse_Plots/plot_INDIV-INDIV/%s_plot'%(os.getcwd(), fileName))

# 			pop.folder_name_list.append(fileName)
			
# 			pop.load_INDIV_JSON_files(fileName)
# 			pop.load_INDIV_MIN_files(fileName)
# 			pop.diff_INDIV_MIN(fileName)

if __name__ == '__main__': 
	lots_o_plots = Filter_Plots_IND_IND()
	lots_o_plots

