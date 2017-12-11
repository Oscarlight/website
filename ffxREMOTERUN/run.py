#!/usr/bin/env python3.5
#### ********** IMPORTANT *************
#### OMG: run from ssh, add -S, tell it not include any path, then added here
#### path is different for different user
#### the last path is used first!! 
import json
import sys
sys.path.append('/home/oscar/Documents/AptanaStudio3Workspace/ffxREMOTERUN')
sys.path.append('/home/oscar/anaconda3/lib/python3.5/site-packages')
# sys.path.append('/home/oscar/anaconda3/lib/python3.5/site-packages/numpy-1.11.1-py3.5.egg-info/')
import numpy as np
import ffx
import csv
# import matplotlib.pyplot as plt
# Scale up the y is y is too small
class InputData():

	def __init__(self, train_file, test_file):
		# read into the data
		train_data = np.genfromtxt(train_file, dtype = float, 
			delimiter=',', skip_header = 1)
		test_data = np.genfromtxt(test_file, dtype = float,
			delimiter=',', skip_header = 1)
		self.train_y = train_data.T[-1]
		self.train_x = (train_data.T[:-1]).T
		self.test_y = test_data.T[-1]
		self.test_x = (test_data.T[:-1]).T

		# read into the names
		with open(train_file, newline='') as f:
  			reader = csv.reader(f)
  			names = next(reader)  # gets the first line
	
		self.names = names[:-1]

		# print(len(self.names))
		# print('Dim of variables: ' + str(self.train_x.shape))
		# print(self.train_x[1])
		# print(self.test_x[1])
		# print('Dim of output' + str(self.train_y.shape))
		# Assertions
		assert len(self.names) == self.train_x.shape[1]
		assert self.train_x.shape[1] == self.test_x.shape[1]
		assert self.train_x.shape[0] == self.train_y.shape[0]
		assert self.test_x.shape[0] == self.test_y.shape[0]

	def scaleY(self, absMax):
		x1 = self.train_y
		x2 = self.test_y
		ratio = absMax / abs(max(x1.min(), x1.max(), key= abs))
		# print('scale ratio is: ' + str(ratio))
		return x1 * ratio, x2 * ratio, ratio

# This creates a dataset from "data.csv"
# train_X = np.array([[0, 1, 2, 3]]).T
# train_y = np.array([0, 1, 4, 9])

# test_X = np.array([[4, 5, 6, 7]]).T
# test_y = np.array([16, 25, 36, 49])

# models = ffx.run(train_X, train_y, test_X, test_y, ["x"])



if __name__ == '__main__':
	# dir = '/home/oscar/Documents/AptanaStudio3Workspace/ffxREMOTERUN/RTD.csv'
	# d = InputData(dir, dir)
	d = InputData(str(sys.argv[1]), str(sys.argv[1]))
	train_y, test_y, ratio = d.scaleY(5)
	isploted = False
	if isploted:
		plt.plot(d.train_x.T[0], d.train_y)
		f = lambda V : 1/ratio * (0.0199 - 2.29*V**2 + 1.46*V - 0.137*V**2 + 0.124*V) / (1.0 + 3.67*V**2 - 3.64*V - 0.261*V + 0.224*V**2)
		y = list(map(f, d.train_x.T[0]))
		plt.plot(d.train_x.T[0], y, 'r')
		plt.show()
	if not isploted:
		models = ffx.run(d.train_x, train_y, d.test_x, test_y, d.names)
		# print('Results:')
		disList = []
		disList.append('Num bases,    Test error (%),         Model\n')
		for model in models:
			# print(model)
			disList.append('%10s, %13s, %25s\n' % 
				('%d' % model.numBases(), '%.4f' % (model.test_nmse * 100.0), model))

		print(json.dumps(disList))
		# with open("/home/oscar/Documents/AptanaStudio3Workspace/ffxREMOTERUN/output.txt", "a") as myfile:
		# 	myfile.write("appended text")
	# print(json.dumps(["IHateit", "NoIloveit"])) # use for debug ssh connection
		## This has be right after print(json.dumps())
		raise SystemExit("End")