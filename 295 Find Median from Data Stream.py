'''
方法1 用插入排序，每次插入都将list有序，则中位数就([len//2]+[(len-1)//2])/2,就行了
寻找插入位置是用二分查找的方法，所以N*O(logN)
'''

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        return (self.nums[len(self.nums)//2]+self.nums[(len(self.nums)-1)//2]) / 2.0