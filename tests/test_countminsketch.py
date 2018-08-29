''' Tests for countminsketch
'''

import unittest
import numpy as np
import mmh3

from countminsketch import CountMinSketch

class TestCountMinSketch(unittest.TestCase):
    ''' General test class for the CMS
    '''
    param_w = 10
    param_d = 3
    seeds = np.random.randint(param_w, size = param_d)

    def test_bad_sketch(self):
        with self.assertRaises(ValueError):
            CountMinSketch(0, 10, seed = seeds)
        with self.assertRaises(ValueError):
            CountMinSketch(10, 0, seed = seeds)

if __name__ == '__main__':
	unittest.main()