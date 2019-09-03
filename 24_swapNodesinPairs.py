class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp = ListNode(0)
        temp.next = head
        cur = temp
        while cur.next.next and cur.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return temp.next
    

#qiu designed
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            first = pre.next
            sec = pre.next.next
            pre.next, sec.next, first.next, pre =sec, first, sec.next, first
        return dummy.next

