# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:08:24 2019

@author: victor
"""
import numpy as np
a = np.random.randint(0, 10, size=(5, 4))
sum = a.sum(axis=1)
print(sum.size)