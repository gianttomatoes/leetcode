# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:26:17 2019

@author: victor
"""
'''
———————————————————————————————————————————————————————————————————————————————
解一:一层循环i，类似快排的左右指针l,r，把i，l，r上的元素都加起来，与target比大小，
就是要注意去重  排序O(nlogn),一层循环O(N),里面两个指针选元素O(N),故总的也是O(N^2),这种方法不用set，空间复杂度O(1)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            
            if i>0 and nums[i] == nums[i-1]:           #在第一层i里去重
                continue
            
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[l]+nums[i]+nums[r]
                if s>0:
                    r -= 1
                elif s<0:
                    l += 1
                else:
                    res.append((nums[i],nums[l],nums[r]))
                    
                    while l<r and nums[l] ==nums[l+1]:            #两个while分别在l和r上去重
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    
                    l+=1
                    r-=1
        return res
    
'''
———————————————————————————————————————————————————————————————————————————————
解二：用set减一层把O(n^3)减到O(n^2)，先sort，来减少判重的损耗
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i, val1 in enumerate(nums[:-2]):
            d = {}
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j, val2 in enumerate(nums[i+1:]):

                if val2 in d:
                    res.add((val1,-val1-val2,val2))
                else:
                    d[-val1-val2] = 1
        return list(res)
    
    
'''
———————————————————————————————————————————————————————————————————————————————
用set，在第一个i也不用判重，但
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i, val1 in enumerate(nums[:-2]):
            d = {}
            for j, val2 in enumerate(nums[i+1:]):

                if val2 in d:
                    res.add((val1,-val1-val2,val2))
                else:
                    d[-val1-val2] = 1
        return list(res)
          

