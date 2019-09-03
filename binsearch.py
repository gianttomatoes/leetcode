# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:14:31 2019

@author: victor
"""

def binsearch(array, x):
    left, right = 0, len(array)-1
    while left<=right:
        mid = left + (right-left)/2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1