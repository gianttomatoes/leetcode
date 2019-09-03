# -*- coding: utf-8 -*-
"""
Created on Sun May 19 14:53:47 2019

@author: victor

"""

'''
———————————————————————————————————————————————————————————————————————————————
解一：
暴力解没啥好说的（直接每k个数），注意一下测试用例为空和len<k的情况
O((n-k+1)*klogk)
'''
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if not nums:
#             return nums
#         ans = [0 for _ in range(len(nums)-k+1)]
#         for i in range(len(nums)-k+1):
#             ans[i] = max(nums[i:i+k])
#         return ans
#
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if len(nums) == 0:
#             return []
#         elif len(nums) <= k:
#             return [max(nums)]
#         else:
#             answer = [0 for i in range(len(nums)-k+1)]
#             for i in range(len(nums)-k+1):
#                 answer[i] = max(nums[i:i+k])
#             return answer
#
# '''
# ———————————————————————————————————————————————————————————————————————————————
# 解二：heap 用heap来做找最大的过程，O((n-k+1)*logk) 维护一个heap 框子每动一次 就在堆里删最左边的元素，加入新元素，更新堆
# 问题在于：最左边不一定是最小的（heap[0]）怎么删他
# '''
#
#
# '''
# ———————————————————————————————————————————————————————————————————————————————
# 解三：O(n) 单调队列/双端队列
# 单调队列就是 从大到小排序 每次加入新的元素之后会把比他小的所有元素都删掉
# '''
#
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         d = collections.deque()
#         answer = []
#         if len(nums) == 0:
#             return answer
#         elif len(nums) <= k:
#             return [max(nums)]
#         else:
#
#             for i,val in enumerate(nums):
#                 # 当一个走出window之外之后，deque最左边的下标记录的就是剩下的window里面最大的了
#                 while d and val > nums[d[-1]]:
#                     d.pop()
#                 d.append(i)
#                 if d[0] == i - k:
#                     d.popleft()
#                 if i >= k-1:
#                     answer.append(nums[d[0]])
#         return answer

# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         if not nums:
#             return []
#         deque, ans = [], []
#         for i, val in enumerate(nums):
#
#             while deque and nums[deque[-1]] < val:  # 把剩下左边比它小的都赶跑，使这个位子前面的一定都比他大
#                 deque.pop()
#             deque.append(i)  # 找到了位子，那么放着
#             # 大的一直都放在前面，只有它出框才让他滚蛋，即走了k步之后，框的边界i-k>=deque[0]了 才让他滚
#             if i - k >= deque[0]:
#                 deque.pop(0)
#             if i >= k - 1:
#                 ans.append(nums[deque[0]])
#         return ans
#
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# solution = Solution()
# print(solution.maxSlidingWindow(nums,k))
#


class Solution:
    def slidingwindow(self, nums, k):
        if not nums:
            return []
        deque = []
        ans = []
        for i, val in enumerate(nums):
            while deque and nums[deque[-1]] < val:
                deque.pop()
            deque.append(i)

            if i-k >= deque[0]:
                deque.pop(0)
            if i >= k-1:
                ans.append(nums[deque[0]])
        return ans


nums = []
k = 3
solution = Solution()
print(solution.slidingwindow(nums,k))