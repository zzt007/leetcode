# 对应习题15，三数之和，难度为中等
'''
    给定一个整数数组nums，判断是否存在三元组[nums[i],nums[j],nums[k]]
    满足 i!=j i!=k j!=k
    同时还满足[nums[i],nums[j],nums[k]] == 0
    请返回所有和为0且不重复的三元组
'''
from typing import List
class Solution:
    def threeSum(self,nums:List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            
            # 跳过相同的元素以避免重复
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while right > left:
                sum_ = nums[i] + nums[left] +nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    while right > left and nums[left] == nums[left+1]:
                        left += 1

                    right -= 1
                    left += 1
            return res