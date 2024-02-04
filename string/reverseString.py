# 对应习题344，难度为简单
'''
    编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组s的形式给出。
    必须要原地修改输入数组，使用O(1)的额外空间解决这一问题。
    输入：s = ["h","e","l","l","o"]
    输出：["o","l","l","e","h"]
'''

# 针对元素交换的问题，目前已经有如下方法：
'''
    1、直接使用函数reverse
    2、链表
    3、双指针对应元素调换
'''
from typing import List
class Solution:
    def reverseString(self,s:List[str]) -> List[str]:
        left = 0
        right = len(s)-1
        while left < (len(s) // 2):
            s[left] , s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s
    
if __name__ == "__main__":
    test = Solution()
    s = ["h","e","l","l","o"]
    output = test.reverseString(s)
    print(output)


