# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:23:19 2019

@author: victor
"""

#word1 = input("Please input first string\n")
#word2 = input("Please input second string \n")
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:        
        len1 = len(word1)
        len2 = len(word2)
        if word1 == "":
            return len2
        if word2 == "":
            return len1
        DPtable = [[0 for i in range(len1+1)] for j in range(len2+1)]
        for i in range(len1+1):
            DPtable[0][i] = i
            
        for i in range(len2+1):
            DPtable[i][0] = i

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1] == word2[j-1]:
                    DPtable[j][i] = DPtable[j-1][i-1]
                else:
                    DPtable[j][i] = min(DPtable[j-1][i],DPtable[j][i-1],DPtable[j-1][i-1]) + 1
        return DPtable[j][i]