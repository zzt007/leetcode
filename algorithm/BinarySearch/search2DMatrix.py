# 对应习题74
'''
    给定一个二维矩阵（mxn），判断是否存在一个目标值，在则返回True，否则返回False；
    该矩阵具有如下特性：
    每行中的整数从左到右升序排列
    每行的第一个整数大于前一行的最后一个整数
'''

# 可以看到，如果将其表示为一个一维数组的话，就是一个升序排列的数组
# 要使用高效的算法来查找的话，可以使用二分查找，是O(logn)
# 重点在于如何将二维数组的索引用一维形式表达

from typing import List
class Solution:
    def __init__(self):
        self.left_index = 0
        self.right_index = 0
    
    def search2DMatrix(self,matrix:List[int],target:int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        self.right_index = row * col -1
        while self.left_index <= self.right_index:
            mid = (self.left_index + self.right_index) // 2
            mid_num = matrix[mid // col][mid % col]
            if mid_num == target:
                return True
            elif mid_num < target:
                self.left_index = mid + 1
            else:
                self.right_index = mid - 1
        return False

if __name__ == "__main__":
    test = Solution()
    input = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 31
    output = test.search2DMatrix(input,target)
    print(output)