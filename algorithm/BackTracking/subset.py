# 对应习题78
'''
    给定一个没有重复元素的集合，找出它的所有子集
'''
from typing import List
class Solution:
    def subsets(self,nums:List[int])->List[List[int]]:
        res = [[]]
        # 按子集可能的长度来遍历
        for i in range(1,len(nums)+1):
            self.backtracking(nums,res,i,0,[])
        return res
    
    def backtracking(self,nums,res,length,index,subset):
        # 基线条件
        if len(subset) == length:
            # 下面这样写是错误的,因为这里还涉及到了拷贝，直接将subset添加，由于其有pop操作，会将值剔除，导致元素个数增加了，但是值是空值
            # res.append(subset)
            res.append(subset[:])
            return
        
        for i in range(index,len(nums)):
            subset.append(nums[i])
            # 从i+1开始是因为集合没有重复元素，所以从下一个开始遍历
            self.backtracking(nums,res,length,i+1,subset)
            # 在回溯过程中需要剔除已有结果的最新元素，否则在回溯到上一级时再往另一条路走时，会多出这个最新元素
            subset.pop()

if __name__ == "__main__":
    test = Solution()
    nums = [1,2]
    output = test.subsets(nums)
    print(output)
    print(len(output))