# 对应习题704
'''
    给定一个n个元素有序(升序的)整型数组nums和一个目标值target，
    写一个函数搜索nums中的target，如果目标值存在返回其下标，否则返回-1.
'''

from typing import List
class Solution:
    def __init__(self) -> None:
        self.low_index = 0
        self.high_index = 0

    def isExist(self,nums:List[int],target:int) -> int:
        if target not in nums:
            return -1
        self.high_index = len(nums) - 1
        while self.low_index <= self.high_index:
            mid = ( self.low_index + self.high_index ) // 2
            # if nums[mid] == target:
            #     return mid
            if nums[mid] > target:
                self.high_index = mid - 1
            elif nums[mid] < target:
                self.low_index = mid + 1
            # 以下else部分可适用于数组中含重复元素，输出重复元素的第一个的下标
            else:
                while nums[mid] == target and nums[mid] == nums[mid-1]:
                    mid -= 1
                return mid


if __name__ == "__main__":
    test = Solution()
    nums = [1,2,4,4,5,6,7,8,9]
    target = 4
    output = test.isExist(nums,target)
    print(output)

