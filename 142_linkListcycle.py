# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:01:35 2019

@author: victor
1.用map的方法，让指针一直走，把每个节点都放到字典里面，判断新来的节点在不在字典里面，return 指针的位置/None
2.用快慢指针 看图2(a+b)=a+b+a+c -> a=c 故先让他们相遇，相遇后从起点再搞个third指针，让slow和third一步一步走，相遇的地方就是起点，返回即可
"""

class LinkNode:
    def __init__(self, x):
        self.val =x
        self.next = None
#List Map       
class Solution:
    def linkedListCycleII(self, head):
        s = []
        while head:
            if head in s:
                return head
            else:
                s.append(head)
                head = head.next
        return None
    
#HashMap
class Solution:
    def detectCycle(self, head):
        visited={}
        while head:
            if visited.get(head):
                return head
            else:
                visited[head] = True
        return None
    
#quick/slow pointers
class Solution:    
    def detectCycle(self, head):
        quick = slow =third = head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if quick is slow:
                while third != slow:
                    third = third.next
                    slow = slow.next
                return slow
        return None