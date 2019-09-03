# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:32:16 2019

@author: victor
"""
'''
解一：建set，然后数set里面的每个字符分别在s和t里面出现的次数，写入字典，判断d1是否等于d2
O(N)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i in set(s):
            d1[i] = s.count(i)
        for j in set(t):
            d2[j] = t.count(j)
        return d1==d2
'''    
——————————————————————————————————————————————————————————————————————————————    
解二：用字典的get方法,get之后+1
'''
def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2


'''
———————————————————————————————————————————————————————————————————————————————
解三：sort，判断sort之后的字符串是否相等，O(NlogN)
'''
def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)