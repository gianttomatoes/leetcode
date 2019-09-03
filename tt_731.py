# # # -*- coding: utf-8 -*-
# # """
# # Created on Wed Jul 31 20:47:43 2019
# #
# # @author: victor
# # """
# #
# # # break只炸一层
# # operator_precedence = {
# #     '(': 0,
# #     ')': 0,
# #     '+': 1,
# #     '-': 1,
# #     '*': 2,
# #     '/': 2
# # }
# #
# #
# # def postfix_convert(exp):
# #     '''
# #     将表达式字符串，转为后缀表达式
# #     如exp = "1+2*(3-1)-4"
# #     转换为：postfix = ['1', '2', '3', '1', '-', '*', '+', '4', '-']
# #     '''
# #     stack = []  # 运算符栈，存放运算符
# #     postfix = []  # 后缀表达式栈
# #     for char in exp:
# #         #        print char, stack, postfix
# #         if char not in operator_precedence:  # 非符号，直接进栈
# #             postfix.append(char)
# #         else:
# #             if len(stack) == 0:  # 若是运算符栈啥也没有，直接将运算符进栈
# #                 stack.append(char)
# #             else:
# #                 if char == "(":
# #                     stack.append(char)
# #                 elif char == ")":  # 遇到了右括号，运算符出栈到postfix中，并且将左括号出栈
# #                     while stack[-1] != "(":
# #                         postfix.append(stack.pop())
# #                     stack.pop()
# #
# #                 elif operator_precedence[char] > operator_precedence[stack[-1]]:
# #                     # 只要优先级数字大，那么就继续追加
# #                     stack.append(char)
# #                 else:
# #                     while len(stack) != 0:
# #                         if stack[-1] == "(":  # 运算符栈一直出栈，直到遇到了左括号或者长度为0
# #                             break
# #                         postfix.append(stack.pop())  # 将运算符栈的运算符，依次出栈放到表达式栈里面
# #                     stack.append(char)  # 并且将当前符号追放到符号栈里面
# #
# #     while len(stack) != 0:  # 如果符号站里面还有元素，就直接将其出栈到表达式栈里面
# #         postfix.append(stack.pop())
# #     return postfix
# #
# # # print(postfix_convert('1+1'))
# # class Node(object):
# #     def __init__(self, val):
# #         self.val = val
# #         self.left = None
# #         self.right = None
# # def create_expression_tree(postfix):
# #     """
# #     利用后缀表达式，构造二叉树
# #     """
# #     stack = []
# #     #print postfix
# #     for char in postfix:
# #         if char not in operator_precedence:
# #             #非操作符，即叶子节点
# #             node = Node(char)
# #             stack.append(node)
# #         else:
# #             #遇到了运算符，出两个，进一个。
# #             node = Node(char)
# #             right = stack.pop()
# #             left = stack.pop()
# #             node.right = right
# #             node.left = left
# #             stack.append(node)
# #     #将最后一个出了即可。
# #     return stack.pop()
# # def inorder(tree):
# #     if tree:
# #         inorder(tree.left)
# #         print(tree.val)
# #         inorder(tree.right)
# #
# # inorder(create_expression_tree(postfix_convert('3+2+1+4*5+1')))
#
# from sklearn.feature_extraction.text import CountVectorizer
# import numpy as np
#
# def jaccard_similarity(s1, s2):
#     def add_space(s):
#         return ' '.join(list(s))
#
#     # 将字中间加入空格
#     s1, s2 = add_space(s1), add_space(s2)
#     # 转化为TF矩阵
#     cv = CountVectorizer(tokenizer=lambda s: s.split())
#     corpus = [s1, s2]
#     vectors = cv.fit_transform(corpus).toarray()
#     # 求交集
#     numerator = np.sum(np.min(vectors, axis=0))
#     # 求并集
#     denominator = np.sum(np.max(vectors, axis=0))
#     # 计算杰卡德系数
#     return 1.0 * numerator / denominator
#
# s1 = '你在干嘛呢'
# s2 = '你在干什么呢'
# print(jaccard_similarity(s1, s2))
# x = '1234'
# y = '34215'
# print([i==j for i,j in zip(x,y)])
# class Person:
#     def __init__(self,new_name):
#         self.name = new_name
#         print("%s 来了" %self.name)
#     def __del__(self):
#         print("%s 走了" %self.name)
# tom = Person("Tom")
# del tom
# class A(object):
#     i = '0'
# class B(A):
#     pass
# class C(A):
#     pass
# B.i = '1'
# A.i = '2'
# print(A.i,B.i,C.i)
for i in range(100,300):
    if i%7 == 6 and i%8 ==8 and i%8==7:
        print(i)
