# 对应leetcode 217

'''
    给定一个数组，如果数组内有重复的元素(出现两次及以上)，则返回true；
    若数组中各个元素都不相同，则返回false 
'''
# 使用集合完成
from typing import List
class Solution:
    def __init__(self) -> None:
        self.set_nums = set()

    def isRepeat(self,nums:List[int])->bool:
        self.set_nums = set(nums)
        len_set = len(self.set_nums)
        len_nums = len(nums)
        if (len_nums - len_set) >= 1:
            return True
        else:
            return False

# 测试
if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3,4,5,1]
    output = test.isRepeat(nums)
    print(output)