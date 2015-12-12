import glob, os
import json 	
import numpy as np
import re
import codecs


class Calling_Doctor_Wavelength:
	def __init__(self):
		x = 'instancely delicious!'
		
		self.refWavelength_list = []
		self.masterWavelength = []
		self.find_masterWavelength()

	def find_masterWavelength(self):
		for file in glob.glob('%s/controlData_AVG_Files/*/refWavelength.json'%os.getcwd()):
			front_part = file.split("/")[-1].split('.')[0]
			with codecs.open(file) as json_data_file: 
				refWavelength = json.load(json_data_file)

			self.refWavelength_list.append(refWavelength)
		
		for x in range(len(refWavelength)): 
			avg_list = []
			for val in range(len(self.refWavelength_list)):
				avg_list.append(self.refWavelength_list[val][x])

			avgNum = np.mean(avg_list)
			self.masterWavelength.append(avgNum)

		print len(self.masterWavelength)
		with open('%s/masterWavelength.json'%os.getcwd(), 'w') as r:
			r.write(json.dumps(self.masterWavelength, sort_keys=True, indent=4, separators=(',', ': ')))

	def find_fileName(self):
		self.folder_name_list = []
		for file in glob.glob("%s/controlData_JSON_Files/*"%os.getcwd()):
			self.fileName = file.split("/")[-1]

			self.folder_name_list.append(self.fileName)
		self.__init__()

if __name__ == '__main__':
	something = Calling_Doctor_Wavelength()
	something.find_fileName()
	print "done"



	