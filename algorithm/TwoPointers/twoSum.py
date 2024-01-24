# 对应习题1，难度为简单
'''
    给定一个整数数组nums和一个整数目标值target，请在数组中找出和为目标值的那两个整数，并返回它们的数组下标
    其中数组元素互不相同
'''

# 之前已经使用哈希表解决过，现在使用双指针来解决
from typing import List
class Solution:
    def twoSum(self,nums:List[int],target:int) -> List[int]:
        left = 0
        right = len(nums) - 1
        # 对无序的数组进行排序，默认为从小到大排序。
        # 但是排完序后，原来元素的位置就乱了，所以在后面需要进行一些处理，让我们返回的是原来数组的元素下标
        nums_sorted = sorted(nums)
        while(left < right):
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                # 这里是用了数组的index方法来查找元素对应的下标
                # 也就是查找目前这个元素在原来没排序的数组的下标
                left_index = nums.index(nums_sorted[left])
                right_index = nums.index(nums_sorted[right]) 
                # 这里是对数组中如果出现重复元素做的一个处理，即让right_index对应元素的下一个重复元素
                if left_index == right_index:
                    right_index = nums[left_index+1:].index(nums_sorted[right]) + left_index + 1
                return [left_index,right_index]
            
            # （目前是有序排序的），当和小于target时，左指针向右移动寻找更大的值
            elif current_sum < target:
                left += 1
            else:
                right -= 1

if __name__ =="__main__":
    test = Solution()
    nums = [3,3]
    target = 6
    output = test.twoSum(nums,target)
    print(output)