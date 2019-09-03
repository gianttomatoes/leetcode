# -*- coding: utf-8 -*-
"""
Created on Sun May 19 14:15:31 2019

@author: victor
维护一个大小为k的小顶堆，实现流式数据第k大元素
输入：k 以及初始数组nums 注:nums的长度可能大于k也可能小于k 要注意想测试用例
1.用nums前k个元素，建立大小为k的小顶堆
2.把剩余初始数组中元素加入堆中，具体为：若元素nums[i]>堆顶，则加入，若元素nums[i]<堆顶
则 它不会改变第k大元素，则不用加入堆

利用heapq这个包来实现 文档：https://docs.python.org/3.0/library/heapq.html#heapq.heapify
"""
# qiu designed
import heapq


class KthLargest(object):


    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.heap = nums[-k:]
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]







import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n = k
        self.nums = nums
        self.heap = nums[0:k]
        heapq.heapify(self.heap)                                       #
        if len(self.nums):
            while k <= len(self.nums)-1:
                if self.nums[k] > self.heap[0]:
                    heapq.heapreplace(self.heap,self.nums[k])
                k += 1

    def add(self, val: int) -> int:
        if len(self.heap)==self.n:
            if self.heap[0] < val:
                heapq.heapreplace(self.heap,val)
        else:
            heapq.heappush(self.heap,val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)