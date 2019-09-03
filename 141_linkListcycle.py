# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
只要有环，两个速度不一样的指针就必会相遇，相遇就说明有环
'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        quick = head
        slow = head
        while quick and slow and quick.next:   # 这个地方quick.next如果不判断，则当quick到达最后一个节点的时候
            quick = quick.next.next            # 满足条件进入循环，但quick.next=None是没有next属性的，求quick.next.next就会报错
            slow = slow.next
            if quick == slow:
                return True
        return False