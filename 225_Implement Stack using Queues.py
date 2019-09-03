# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:30:47 2019

@author: victor
思路贼简单，就是queue1拿来装入栈的元素，每次从栈时，队首入队，top元素就是queue1[0],
出栈时，把除了queue1[0]之外的元素都出队到queue2中，再从queue2中入队（即转一圈，现在原来queue[0]在队尾，pop即可）
用pop(0)和append的方向比用insert(0,x)和pop()的效率要高一些
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(len(self.stack1[0:-1])):
            temp = self.stack1.pop(0)
            self.stack2.append(temp)
        for _ in self.stack2:
            temp = self.stack2.pop(0)
            self.stack1.append(temp)
             
        return self.stack1.pop(0)
            

    def top(self) -> int:
        """
        Get the top element.
        """
        
        return self.stack1[-1]
            

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.stack1) == 0:
            return True
        else:
            return False