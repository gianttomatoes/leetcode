# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:52:57 2019

@author: victor
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:                
                temp = self.stack1.pop()
                self.stack2.append(temp)
                
        
        return self.stack2.pop()
    
    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
                
        return self.stack2[-1]
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not len(self.stack1) and not len(self.stack2):
            return True
        else:
            return False
