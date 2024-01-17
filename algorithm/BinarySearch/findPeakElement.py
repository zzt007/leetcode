# 对应习题162
'''
    给定一个输入数组，其中相邻元素不相等，需要找到峰值元素并返回其索引
    数组可能包含多个峰值，返回任意一个即可
    假设nums[-1] = nums[n] = -∞
'''

# 使用二分查找 + 迭代爬坡的方法，使其时间复杂度为O(logn)
# 不过相较于三个元素做整体来遍历的方法，本方法只能找到任意的一个峰值

from typing import List
class Solution:
    def __init__(self) -> None:
        self.low_index = 0
        self.high_index = 0
        self.mid_index = 0 
    
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        self.low_index = 0
        self.high_index = len(nums) - 1

        while self.low_index <= self.high_index:
            self.mid_index = (self.low_index + self.high_index) // 2
            if self.mid_index == -1 or self.mid_index == len(nums):
                return nums[self.mid_index]
            if nums[self.mid_index] > nums[self.mid_index - 1] and nums[self.mid_index] > nums[self.mid_index + 1]:
                return self.mid_index
                
            if nums[self.mid_index] < nums[self.mid_index + 1]:
                self.low_index = self.mid_index + 1
            else:
                self.high_index = self.mid_index - 1
        return self.mid_index

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         n = len(nums)

#         # 辅助函数，输入下标 i，返回 nums[i] 的值
#         # 方便处理 nums[-1] 以及 nums[n] 的边界情况
#         def get(i: int) -> int:
#             if i == -1 or i == n:
#                 return float('-inf')
#             return nums[i]
        
#         left, right, ans = 0, n - 1, -1
#         while left <= right:
#             mid = (left + right) // 2
#             if get(mid - 1) < get(mid) > get(mid + 1):
#                 ans = mid
#                 break
#             if get(mid) < get(mid + 1):
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return ans


if __name__ == "__main__":  
    test = Solution()
    nums = [1,2,3,1]
    output = test.findPeakElement(nums)
    print(output)