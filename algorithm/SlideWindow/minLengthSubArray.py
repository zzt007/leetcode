# 对应习题209
'''
    给定一个含有n个正整数的数组和一个正整数target，找出该数组中满足其和>=s的长度最小的连续子数组
    并返回其长度，如果不存在符合条件的子数组，返回0
'''

from typing import List
class Solution_v1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_slideWindow = 1
        target_bigger_nums_flag = 0
        if sum(nums) < target:
            return target_bigger_nums_flag
        while len_slideWindow <= len(nums):
            count_cycle = len(nums) - len_slideWindow + 1
            for i in range(count_cycle):
                if sum(nums[i:i+len_slideWindow]) >= target:
                    return len_slideWindow
            len_slideWindow += 1 

if __name__ == "__main__":
    test = Solution_v1()
    nums = [2,3,1,2,4,3]
    target = 3
    output = test.findArray(nums,target)
    print(output)

# 上述写法(暴力法)在力扣测试中超出时间限制，说明时间复杂度太高了，为O(n²)
    
# 下面采用滑动窗口法进行，也可以说是双指针法，时间复杂度为O(n)
class Solution:
    def minSubArrayLen(self,target:int,nums:List[int])->int:
        if nums is None or len(nums) == 0:
            return 0
        result = len(nums) + 1 # 一般将结果设为不可能的值，这里不设为0是为了不影响后面取最小的操作
        total = 0
        i,j = 0,0
        while j < len(nums):
            total += nums[j]
            while total >= target:
                result = min(result,j-i+1)
                total -= nums[i]
                i += 1
            j += 1
        return 0 if result == len(nums) + 1 else result # result == len(nums) + 1 意味着没有找到有效的答案
    
