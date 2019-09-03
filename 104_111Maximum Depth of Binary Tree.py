'''
104 递归，BFS/DFS
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))



'''
111 BFS
类似于102 用level记录下层数，逐层遍历，找到第一个叶子节点，返回该节点的层数
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        level = 1
        while queue:
            num = len(queue)
            for i in range(num):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

'''
也可以用递归，但是要注意并不是直接返回左右子树中层数少的再+1就行，因为当没有左子树时，它不是叶子节点，返回0+1就GG了
但是加一句就完事了，只需排除掉该节点只有一个孩子的情况，直接返回另一个节点的高度就ok
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.right),self.minDepth(root.left))