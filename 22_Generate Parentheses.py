'''
22
qiu：
第一个想到的是根据n全排列，然后用判断括号是否合法的方法来筛,是可以的，这个要取决于你怎么实现全排列，用bit位然后replace的话
复杂度O(2**n),比全排列的阶乘好 能通过
'''



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n *= 2
        full_permutation = [bin(i)[2:].rjust(n, '0') for i in range(2 ** n)]    # 取2*n位二进制数，并且长度不够的补零
        for i in range(len(full_permutation)):                                  # 把0 1 替换成'('')'
            full_permutation[i] = full_permutation[i].replace('0', '(')
            full_permutation[i] = full_permutation[i].replace('1', ')')
        res = []

        for i in full_permutation:
            ans = self.validparetheses(i)
            if ans:
                res.append(i)
        return res

    def validparetheses(self, s):
        right = {')': '('}
        stack = []
        for i in s:
            if not i in right:
                stack.append(i)
            else:
                if not stack or right[i] != stack.pop():
                    return False
        if not stack:
            return True
        else:
            return False


'''
解二 递归
其实只要理解了合法生成括号的几点就能写出简单的递归了
1.左括号一定是先出现的 所以递归时先写左括号 但也不能无限制全写左括号 所以有n的限制
2.右括号出现 其实右括号不管出现在哪 只要前面有左括号 第一个右括号一定是合法的 总结下来就是只要前面的左括号数比右括号数多
那一定是合法的
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.gen(0, 0, n, '')
        return self.res

    def gen(self, left, right, n, result):
        if left == n and right == n:
            self.res.append(result)
            return
        # 左括号要先
        if left < n:
            self.gen(left + 1, right, n, result + '(')
        if left > right and right < n:
            self.gen(left, right + 1, n, result + ')')