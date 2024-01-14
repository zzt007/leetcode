# 对应leetcode 217

'''
    给定一个数组，如果数组内有重复的元素(出现两次及以上)，则返回true；
    若数组中各个元素都不相同，则返回false 
'''
from typing import List
class Solution:
    def __init__(self) -> None:
        self.hashtable = {}

    def findRepeatElement(self,nums:List[int]) -> bool:
        for num in nums:
            if num in self.hashtable:
                self.hashtable[num] += 1
            else:
                self.hashtable[num] = 1
        for key,value in self.hashtable.items():
            if value >= 2:
                return True
        return False
    
if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3,4,5,6,7,8,9,9]
    output = test.findRepeatElement(nums)
    print(test.hashtable)
    print(output)