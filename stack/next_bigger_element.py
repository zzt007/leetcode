# 对应leetcode 496
'''
    给定两个没有重复元素的数组nums1和nums2，其中nums1是nums2的子集。
    找到nums1中每个元素在nums2中的下一个比其大的值。
    nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素
    如果不存在，对应位置输出 -1  
'''

from typing import List
class Solution:
    def __init__(self):
        self.stack = []
        self.result = []

    def reverse_array_and_push_on_stack(self,nums:List[int]):
        nums.reverse()
        for i in nums:
            self.stack.append(i)
        return self.stack
    
    def findNextGreaterElement(self,nums1:List[int],nums2):
        for j in nums1:
            if j >= nums2[-1]:
                nums2.pop()
                self.result.append(-1)
            else:
                self.result.append(nums2[-1])
        return self.result

if __name__ == '__main__':
    test = Solution()
    nums1 = [4,1,2,3]
    nums2 = [1,5,3,4,2]
    stack_nums2 = test.reverse_array_and_push_on_stack(nums2)
    result = test.findNextGreaterElement(nums1,stack_nums2)
    print(result)

