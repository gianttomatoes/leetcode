'''
102 BFS/DFS
用BFS更适合层次遍历的思路
用队列实现，只要队列不为空就出队，并且把出队节点的左孩子和右孩子都入队
但这里要注意输出格式是要一层一层的，那要用个level list来分别装每一层的，就要先知道每一层有多少个
在每一次while 执行完后，上一层的节点全部出队，那么可以用len(queue)来找到下一层所有节点的个数
通过for来控制循环次数就行

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

'''
DFS
DFS是沿着一条边一直走到最底，利用栈或者递归(实际也是系统栈)，那么在DFS时就要记录层数，把每一层的元素append到每一层的list里
要注意的是，如果你第一次来到这一层(第一次递归到第n层)，res数组里是没有该层的list的，所以要创建一个[]
这里的res是一个二维数组
然后每次在一条路径中搜索时，把第一层的append到res[0]，第二次res[1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.DFS(root, 0)
        return self.res

    def DFS(self, root, level):
        if not root:
            return
        # 如果第一次下到这一层就给他创建一个[]
        if level > len(self.res) - 1:
            self.res.append([])
        self.res[level].append(root.val)
        if root.left:
            self.DFS(root.left, level + 1)
        if root.right:
            self.DFS(root.right, level + 1)