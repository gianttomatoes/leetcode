# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:42:03 2019

@author: victor
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<=3:
            return sum(nums)
        res = 0
        nums.sort()
        closest = 9999
        for i in range(len(nums)-2):
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            
            while l<r:
                s = (nums[i]+nums[l]+nums[r])-target
                if abs(s)<closest:
                    closest = abs(s)
                    res = (nums[i]+nums[l]+nums[r])
                if s >0:
                    r -= 1
                if s <0:
                    l+=1
                if s ==0:
                    return nums[i]+nums[l]+nums[r]
                
        return res