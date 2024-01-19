# 对应习题169
'''
    给定一个大小为n的数组，找到其中的多数元素。
    多数元素的定义：出现次数大于n/2次的元素。
    假设数组非空，且给定的数组总是存在多数元素。
'''

# 可以使用哈希表法解决，也比较容易
# 下面使用分治法解决

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.getMajority(nums,0,len(nums)-1)
    
    def getMajority(self,nums,left,right):
        # 基线条件，即划分到只有一个元素
        if left == right:
            return nums[left]
        # 递归条件
        mid = (left + right) // 2
        leftMajority = self.getMajority(nums,left,mid)
        rightMajortiy = self.getMajority(nums,mid+1,right)
        # 如果左右众数一样，则可以直接返回这两个区间的众数
        if leftMajority == rightMajortiy:
            return leftMajority
        # 如果左右众数不同，则需要对比两众数在数组里谁出现的多来确定这两个区间的众数是谁
        else:
            left_count = 0
            right_count = 0
            # right是下标=数组长度-1，现要加回去
            for i in range(left,right+1):
                if nums[i] == leftMajority:
                    left_count += 1
                elif nums[i] == rightMajortiy:
                    right_count += 1
            return leftMajority if left_count > right_count else rightMajortiy

if __name__ == "__main__":
    test = Solution()
    nums = [2,1,1,1,3,2,1]
    output = test.majorityElement(nums)
    print(output)