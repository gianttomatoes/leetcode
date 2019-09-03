# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:39:40 2019

@author: victor
"""

import collections


def heapSort(A):
    #完全二叉树下标从1开始时有：最后一个孩子节点的双亲为len/2向下取整，而数组是从0开始的，故用deque先右移一位
    deque = collections.deque(A)
    deque.appendleft(0)
    
    #下面是heapSort主程序
    length = len(deque) - 1   #为了使用完全二叉树的性质，右移了一位
    lastSubTree = length//2
    #把序列先做成大顶堆，从len/2 开始依次调整子树
    for i in range(lastSubTree):
        heapAdjust(deque,lastSubTree-i,length)
        
    #把每轮的大顶交换到队尾，即输出，然后调整堆，使其保持大顶堆
    for i in range(length):
        deque = swap(deque,1,length-i)
        heapAdjust(deque,1,length-i-1)     #每一轮会换一个到队尾，故要-i，第一轮时换下来队尾就是max了故-1
    return [deque[i] for i in range(1,length+1)]           #把从下标1到最后一个的元素输出

def swap(List, i, j):
    List[i], List[j] = List[j], List[i]
    return List

def heapAdjust(List, startRoot, end):
    temp = List[startRoot]
    i = startRoot
    j = startRoot*2
    
    while j <= end:
        if j<end:   #若节点i有左数也有右子树，则j赋值为较大的孩子下标
            j = j if List[j]>List[j+1] else j+1
        if List[j] > temp:    #若孩子比双亲大，则交换，并且继续往下，孩子作为根节点，看孩子的孩子是否满足大根堆的定义
            List[i] = List[j]
            i = j
            j = 2*i
        else:
            break
    List[i] = temp        #找到交换之后根节点应该在的位置，与该位置上的元素交换
            