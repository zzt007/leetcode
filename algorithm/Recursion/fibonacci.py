# 对应习题509
'''
    给定一个n值，计算斐波那契数F(n)
    F(n) = F(n-1) + F(n-2)
'''

class Solution:
    def fib(self,n:int)->int:
        if n < 2:
            return 0 if n==0 else 1
        res = self.fib(n-1) + self.fib(n-2)
        return res
    

if __name__ == "__main__":
    test = Solution()
    n = 5
    output = test.fib(5)
    print(output)