# Count Min Sketch 

import numpy as np
import random
import mmh3

class CountMinSketch(object):

		def __init__(self, width, depth, seeds):
				self.w = width  # width of table
				self.d = depth  # depth of table (no. of hash functions)
				self.table = np.zeros([depth,width])  # create empty table
				self.seeds = seeds # np.random.randint(w, size = d) // create some seeds

		def increment(self, key):
				for i in range(0, self.d):
					index = mmh3.hash(key, self.seeds[i]) % self.w
					self.table[i,index] = self.table[i,index]+1

		def estimate(self, key):
				minEstimate = self.w
				for i in range(0, self.d):
					index = mmh3.hash(key, self.seeds[i]) % self.w
					if self.table[i, index] < minEstimate:
						minEstimate = self.table[i, index]

				return minEstimate

		def merge(self, newCMS):
				return self.table + newCMS


# tests for CMS
def test_countmin_basic():
    seedList = np.random.randint(10, size = 3)
    s = CountMinSketch(width = 10, depth = 3, seeds = seedList)
    s.increment("peter")
    s.increment("xenopoulos")

    assert s.estimate("peter") == 1
    assert s.estimate("xenopoulos") == 1

def main():
	test_countmin_basic()

main()
