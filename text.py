# # import sys
# # import numpy as np
# # import math
# #
# #
# # h,w = sys.stdin.readline().split()
# # h, w = int(h),int(w)
# # image = []
# # for i in range(h):
# #     line = sys.stdin.readline().split()
# #     values = list(map(int, line))
# #     image += values
# # image = np.array(image).reshape(h, w)
# #
# # length = int(sys.stdin.readline())
# # kernal = []
# # for i in range(length):
# #     line = sys.stdin.readline().split()
# #     values = list(map(int, line))
# #     kernal += values
# # kernal = np.array(kernal).reshape(length,length)
# # ans = [0] * (h-length+1)*(w-length+1)
# # ans = np.array(ans).reshape(h-length+1, w-length+1)
# # for i in range(h-length+1):
# #     for j in range(w-length+1):
# #         ans[i][j] = math.floor(sum(sum(image[i:i+length,j:j+length]*kernal)))
# #
# # for i in range(ans.shape[0]):
# #     s = ''
# #     for j in range(len(ans[i])):
# #         s += str(ans[i,j])
# #         s += ' '
# #     print(s)
# # # product = kernal*image
# # # ans = math.floor(sum(sum(product)))
# # print(ans)
# # print(type(values))
# # print(values)
# # print(image)
# # print(kernal)
# import itertools
#
#
# def validparetheses(s):
#     right = {')': '('}
#     stack = []
#     for i in s:
#         if i not in right:
#             stack.append(i)
#         elif not stack or right[i] != stack.pop():
#
#             return False
#     if not stack:
#         return True
#     else:
#         return False
#
# s1 = '()'
# s2 = s1 * 3
# full_permutation = []
# for i in itertools.permutations(s2, len(s2)):
#     full_permutation.append("".join(i))
# print(len(full_permutation))
# res = []
#
# for i in full_permutation:
#     ans = validparetheses(i)
#     if ans:
#         res.append(i)
# print(list(set(res)))
# a = 'hello'
# b=[1,2]
# print('a and b is{}'.format(a and b))
# print('a or b is {}'.format(a or b))

n=3
a = [bin(i)[2:].rjust(n,'0') for i in range(2**n)]
print(a)