# 对应leetcode 283
'''
    给定一个数组，需要将数组中所有的0移动到数组的末尾，同时保持非零元素的相对顺序不变
    必须要在原数组上操作，不能拷贝额外数组，尽量减少操作次数
'''

# 单次测试
# input = [0,1,0,3,12,0,0,6,7,8]
# not_zero_index = 0
# count_zero = 0
# for i in range(0,len(input)):
#     if input[i] != 0:
#         input[not_zero_index] =input[i]
#         not_zero_index += 1
#     else:
#         count_zero += 1
# input[(len(input)-count_zero):] = [0] * count_zero
# print(input)

# 写成类的形式
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        not_zero_index = 0
        for num in nums:
            if num != 0:
                nums[not_zero_index] = num
                not_zero_index += 1
        for i in range(not_zero_index,len(nums)):
            nums[i] = 0
        return nums
        # 或者如下写法也可以
        # nums[not_zero_index:] = [0] * (len(nums)-not_zero_index-1)
        # return nums

if __name__ == '__main__':
    solution = Solution()
    input = [0,1,0,3,12,0,0,6,7,8]
    output = solution.moveZeroes(input)
    print(output)
    
# 小结，单次测试中引入了两个计数器，不如答案中只有一个计数器