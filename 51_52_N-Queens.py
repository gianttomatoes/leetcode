class Solution:
    def solveNQueens(self, n):
        self.res = []
        self.cols, self.sums, self.minus = [],[],[]
        self.dfs(n, 0, [])
        return self.lastprint(self.res,n)

    def dfs(self, n, row, cur_position):
        if row >= n:
            self.res.append(cur_position)
        # 每一行只有一个皇后，所以每一层递归就是在当前行中找合适的位置放queen
        for col in range(n):
            if col in self.cols or row+col in self.sums or row-col in self.minus:
                continue
            self.cols.append(col)
            self.sums.append(row + col)
            self.minus.append(row-col)
            # cur_position.append([row, col])
            self.dfs(n, row + 1, cur_position + [[row, col]])
            self.cols.remove(col)
            self.sums.remove(row + col)
            self.minus.remove(row - col)

    def lastprint(self, res,n):
        last = []
        for i in res:
            nth = []

            for j in range(n):

                s = i[j][1]*"." + "Q" + (n-i[j][1]-1)*"."
                nth.append(s)
            last.append(nth)
        return last
solution = Solution()
print(solution.solveNQueens(4))