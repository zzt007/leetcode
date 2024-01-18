# 对应习题1456
'''
    给定字符串s和整数k，返回字符串中长度为k的单个子字符串中可能包含的最大元音字母数
    元音字母为：{a,e,i,o,u}
'''

class Solution:
    def maxVowels(self,s:str,k:int)->int:
        if s is None or len(s) == 0 or len(s) < k:
            return 0
        hashset = set(['a', 'e', 'i', 'o', 'u'])
        res = 0
        count = 0
        for i in range(0,k):
            if s[i] in hashset:
                count += 1
        res = max(res,count)

        for i in range(k,len(s)):
            if s[i-k] in hashset:
                count -= 1
            if s[i] in hashset:
                count += 1
            res = max(res,count)
        return res

if __name__ == '__main__': 
    test = Solution()
    s = "abciiidef"
    k = 3
    output = test.maxVowels(s,k)
    print(output)