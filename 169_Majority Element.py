# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:07:22 2019

@author: victor
"""
'''
用set找出元素，用count计数O(N)
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxim = 0
        s = set(nums)
        for i in s:
            if maxim<nums.count(i):
                maxim = nums.count(i)
                res = i
        return res

'''
sort 然后直接找中间的元素
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


'''
利用字典，遍历nums，每过一个把dic中对应key的value加一，这里给出了一种从零构建字典的方法，可以学学
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                count = dic[i]
            else:
                count = 0
            count += 1
            dic[i] = count

        return max(dic, key=dic.get)