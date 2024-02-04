# 对应习题541
'''
    给定一个字符串s和一个整数k，从字符串开头算起，
    每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
    如果剩余字符少于 k 个，则将剩余字符全部反转。
    如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
'''

# 设置一个计数器count，先看有几个2k段，都统一处理；然后再看对2k求余后的数目是在<k还是 k ~ 2k之间
from typing import List
class Solution:
    def reverseString(self,s:str,k:int) -> str:
        def reverse_substring(text):
            left = 0
            right = len(text) - 1
            while left < right:
                text[left],text[right] = text[right],text[left]
                left += 1
                right -= 1
            return text
        res = list(s)
        # 关键所在，对于这种一段一段处理的，我们在遍历的时候可以成段遍历
        for cur in range(0,len(s),2*k):
            res[cur:cur+k] = reverse_substring(res[cur:cur+k])
        return ''.join(res)
    
if __name__ == "__main__":
    test = Solution()
    s = "abcdefg"
    k = 2
    output = test.reverseString(s,k)
    print(output)