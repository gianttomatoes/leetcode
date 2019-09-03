'''
找两个节点的最近公共祖先其实就是找一棵树，两个节点分别在这棵树的左子树和右子树上，那么根节点就一定是它的最近公共祖先
1.递归实现：从根节点开始，分别在左右子树上找p,q。如果左边返回为空，则说明都在右边那么在右边接着找
，直到找到一个节点，p，q分别在他的左右子树上，返回该节点 完成
或者直到找到p或者q了都没能满足pq在两边的条件，那么p是q祖先或者反之，那返回先找到的那个即可

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left == None:
            return right
        elif right == None:
            return left
        else:
            return root




'''
235  如果树是一颗二叉搜索树，那么就可以直接用节点val的值来判断它在左子树还是右子树了，相比236题，必须要遍历找到p或者q
，才能了解它在前面递归的节点的左子树还是在右子树，减少了很多递归的次数
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root or p == root or q == root:
        #     return root
        while root:
            if p.val<root.val and q.val <root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:   # 这里必须要用elif 因为如果用if-if-else的话 就变成 不在右边就返回root
                root = root.right
            else:
                return root
