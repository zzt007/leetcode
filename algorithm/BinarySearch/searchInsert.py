# 对应习题35
'''
    给定一个n个元素有序(升序的)整型数组nums和一个目标值target，
    写一个函数搜索nums中的target，如果目标值存在返回其下标，否则返回其按顺序插入的位置.
'''

from typing import List
class Solution:
    def __init__(self) -> None:
        self.low_index = 0
        self.high_index = 0
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.low_index = 0
        self.high_index = len(nums) - 1
        while self.low_index <= self.high_index:
            mid = (self.low_index + self.high_index) // 2
            if target in nums:
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    self.low_index = mid + 1
                elif nums[mid] > target:
                    self.high_index = mid - 1
            else:
                if nums[mid] < target:
                    self.low_index = mid + 1
                elif nums[mid] > target:
                    self.high_index = mid
                return self.high_index - 1
            
if __name__ == "__main__":
    test = Solution()
    nums = [1,3,4,6,7]
    target = 5
    output = test.searchInsert(nums, target)
    print(output)