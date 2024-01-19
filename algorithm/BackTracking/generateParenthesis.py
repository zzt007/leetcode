# 对应习题22
'''
    parenthesis是圆括号的意思,若要泛指括号则用bracket;
    给定一个正整数n,代表要生成括号的对数.
    设计一个函数能够用于生成所有可能的且有效的括号对
'''

# 使用回溯法解决，打断点逐过程看回溯
from typing import List
class Solution:
    def generateParenthesis(self,n:int)-> List[str]:
        res = []
        self.backtracking(n,res,0,0,"")
        return res
    
    def backtracking(self,n,res,left_num,right_num,s):
        if right_num > left_num:
            return
        
        if (left_num == n and right_num == n):
            res.append(s)
            return
        
        if left_num < n:
            self.backtracking(n,res,left_num+1,right_num,s+"(")
        
        if right_num <left_num:
            self.backtracking(n,res,left_num,right_num+1,s+")")

if __name__ == "__main__":
    test = Solution()
    n = 2
    output = test.generateParenthesis(n)
    print(output)