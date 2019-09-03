# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:41:28 2019

@author: victor
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n & 1:    #判断最后一位是0还是1   n & n-1 把最后一位0消掉
                count+=1
            n >>= 1
        return count
    
    
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n :
            count += 1
            n = n&(n-1)          #把最后一个1消掉
        return count