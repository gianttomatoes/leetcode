'''
50_分治，位运算
要求一个数的n次方，可以利用分治的办法，递归为算她的n//2次方，则复杂度O(logn),
若n为奇数则算（n//2）*（n//2）*x，偶数则算（n//2）*（n//2）
但这里要注意，（n//2）*（n//2）最好用myPow(x*x,n//2)来实现，若用myPow(x,n//2)*myPow(x,n//2)则要开两个空间，算两次
会time limit exceed

'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n%2:
            return self.myPow(x*x,n//2)*x
        else:
            return self.myPow(x*x,n//2)


'''
如果要求不用递归，则要用位运算，即把n化为二进制位，只要看哪些位上的bit是1，则就把该位的位权乘上去
如： 5 =      0 1 0  1b
     3^5 = 3^(0*2^3)*3^(1*2^2)*3^(0*2^1)*3^(1*2^0)
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n
        res = 1                 # 每个二进制位有不同的位权，如果该位为1则代表该位为2^i,这里是求幂，所以若为1就乘一个x
        while n:                # 为了判断该位是否为1，则每次右移一位，同时位权乘以x
            if n&1==1:          # n与上1 其实是n&00000001，目的是判断最右边的一位是否为1，也可以用来判断是否为奇数
                res *= x
            x *= x
            n >>= 1             # 右移一位
        return res