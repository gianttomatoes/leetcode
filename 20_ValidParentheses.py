# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:50:46 2019

@author: victor
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rightPare = {')':'(', '}':'{',']':'['}
        top = -1
        for i in s:
            if i in rightPare and top != -1:
                if rightPare[i] == stack[top]:
                    top -= 1
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i) 
                top += 1
        if top == -1:
            return True
        else:
            return False

class Solution:
    def isValid(self, s: str) -> bool:
        left = {'}':'{',']':'[',')':'('}
        stack = []
        for i in s:
            if i not in left:
                stack.append(i)
            else:
                if not stack:
                    return False
                right = stack.pop()
                if not left.get(i) == right:
                    return False
        if stack:
            return False
        else:
            return True
        
        
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rightPare = {')':'(', '}':'{',']':'['}
        for i in s:
            if i not in rightPare:
                stack.append(i)
            elif not stack or rightPare[i] != stack.pop():
                return False
        return not stack
'''