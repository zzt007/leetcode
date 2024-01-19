# 对应习题53
'''
    给定一个数组，求出一个具有最大和的连续子数组（子数组至少包含一个元素）
    返回最大和。
    注意：子数组是数组的一个连续部分
'''

# 使用分治法
from typing import List
class Solution:
    def maxSubArray(self,nums:List[int])->int:
        return self.getMax(nums,0,len(nums)-1)
    
    def getMax(self,nums:List[int],left,right):
        # 基线条件
        if left == right:
            return nums[left]
        # 递归条件
        mid = (left + right) // 2
        left_sum = self.getMax(nums,left,mid)
        right_sum = self.getMax(nums,mid+1,right)
        cross_sum = self.crossSum(nums,left,right)
        return max(left_sum,right_sum,cross_sum)
    
    def crossSum(self,nums,left,right):
        mid = (left + right) // 2
        # 从中间到左端点
        left_sum = nums[mid]
        left_max = left_sum
        # 向左走，range函数的用法（start,stop,step），step为-1时，代表左开右闭；一般step默认为1，是代表左闭右开
        # 这里从mid-1 到left，由于是左开右闭的，为了达到left处，所以写成left-1
        for i in range(mid-1,left-1,-1):
            left_sum += nums[i]
            left_max = max(left_sum,left_max)

        # 从中间到右端点
        right_sum = nums[mid+1]
        right_max = right_sum
        for i in range(mid+2,right+1):
            right_sum += nums[i]
            right_max = max(right_sum,right_max)

        return left_max + right_max
    
if __name__ == "__main__":
    test = Solution()
    nums = [1,3,4,-1,-3]
    output = test.maxSubArray(nums)
    print(output)