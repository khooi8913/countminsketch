''' This module contains the class necessary to implement CountMinSketch

@author: Peter Xenopoulos
@website: www.peterxeno.com
'''

import numpy as np
import random
import mmh3

class CountMinSketch(object):
	''' Class for a CountMinSketch data structure
	'''
	def __init__(self, width, depth, seed):
		''' Method to initialize the data structure
		@param width int: Width of the table
		@param depth int: Depth of the table (num of hash func)
		@param seeds int: Random seed
		'''
		self.w = width  # width of table
		self.d = depth  # depth of table (no. of hash functions)
		self.table = np.zeros([depth,width])  # create empty table
		self.seed = seed # np.random.randint(w, size = d) // create some seeds

	def increment(self, key):
		''' Method to add a key to the CMS
		@param key str: A string to add to the CMS
		'''
		for i in range(0, self.d):
			index = mmh3.hash(key, self.seeds[i]) % self.w
			self.table[i,index] = self.table[i,index]+1

	def estimate(self, key):
		''' Method to estimate if a key is in a CMS
		@param key str: A string to check
		'''
		minEstimate = self.w
		for i in range(0, self.d):
			index = mmh3.hash(key, self.seeds[i]) % self.w
			if self.table[i, index] < minEstimate:
				minEstimate = self.table[i, index]

		return minEstimate

	def merge(self, newCMS):
		''' Method to combine two count min sketches
		@param newCMS CountMinSketch: Another CMS object
		'''
		return self.table + newCMS
