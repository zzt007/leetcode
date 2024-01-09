# 对应leetcode 485
'''
    给定一个二进制数组，即元素只有0和1，计算其中最大的连续1的个数
    例子：input = [1,1,0,1,1,1] output = 3
'''
# 单次测试
# input = [1,1,0,1,1,1,0,1,1,1,1]
# count = 0
# result = 0
# for i in input:
#     if i == 1:
#         count += 1
#     else:
#         result = count
#         count = 0
# output = max(result,count)
# print(output)

# 写成类的形式，封装
from typing import List # 若不引入该类型，无法直接使用
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        count = 0 
        result = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                result = count
                count = 0
        return max(result,count)

if __name__ == '__main__':
    input = [1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
    solution = Solution()
    output = solution.findMaxConsecutiveOnes(input)
    print(output)