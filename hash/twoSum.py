# 对应习题1，难度为简单
'''
    给定一个整数数组nums和一个整数目标值target，请在数组中找出和为目标值的那两个整数，并返回它们的数组下标
    其中数组元素互不相同
'''
from typing import List
class Solution:
    def twoSum(self,nums:List[int],target:int) -> List[int]:
        hash = {}
        # 枚举数组的下标和元素
        for key,value in enumerate(nums):
            # 这里是把值作为hash的key，下标作为hash的val
            # 由于是两数之和，所以要找到另外一个加数是否已经在hash里，如果是，则返回这两个加数的下标，否则将此时遍历的数和下标存入hash中
            if target - value in hash:
                return [hash[target-value],key]
            hash[value] = key
        return []


