'''
思路1 要判断它是不是二叉搜索树，只需要中序遍历，然后看结果是不是递增的就行，这里注意一下判断递增的哪一行


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.res = []
        self.inorder(root)
        return all([self.res[i] < self.res[i + 1] for i in range(len(self.res) - 1)])

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)