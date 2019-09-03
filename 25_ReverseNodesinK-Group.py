# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:34:14 2019

@author: victor
"""

'''    
利用24题swapinPairs的想法,先去看24题qiu的解法
代码结构为：
|
|每一轮进k个节点，类似两两反转中的cur.next和cur.next.next,用flag来表示链表后面是否存在k个节点
|用left和right指针来记录这k个节点的第一个和最后一个(因为翻转之后要把前后都连起来)
|，翻完之后都把最后一个节点记录为pre用来连接下一轮的k个节点
|
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head
        pre = last = dummy
        flag = 1
        for _ in range(k):
            if not last.next:
                flag = 0
                return head
            last = last.next
        while flag:
            last = self.reverse_list(pre, k)
            pre = last
            if pre:
                for _ in range(k):
                    if not last.next:
                        flag = 0
                        break
                    last = last.next
        return dummy.next

    # 反转k个节点的函数，注：pre是上一个批次里的最后一个，所以dummy.next要连到翻完之后的第一个上
    # left是原本的第一个，但翻完之后是最后一个，所以要连到下一个批次的第一个上
    # 即cur(循环完最后一个之后pre所在位置是本批次最后一个，cur是下批次第一个)
    def reverse_list(self, pre, k):
        dummy = pre
        cur = left = pre.next
        for _ in range(k):
            cur.next, cur, pre = pre, cur.next, cur
        dummy.next = pre
        left.next = cur
        return left



#standard solution
class Solution(object):   
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
    
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next 
            
#qiu's solution
class Solution(object):   
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        tail = dummy
        left = right = head
        dummy.next = head
        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1
            if count == k:
                cur, pre = left, None
                for _ in range(k):
                    cur.next, pre, cur = pre, cur, cur.next
                tail.next, tail, left = pre, left, right
            else:
                tail.next = left
                return dummy.next
        