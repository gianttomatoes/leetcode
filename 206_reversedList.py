# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur , pre = head , None
        while cur:
            cur.next ,pre , cur= pre , cur, cur.next
        return pre

# 不用python的连续赋值，可以移植到c的方法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            nextpoint = cur.next
            cur.next = pre
            pre = cur
            cur = nextpoint
        return pre