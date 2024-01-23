# 对应习题59
'''
    给定一个正整数n，生成一个包含1到n²所有元素，且元素按顺时针顺序螺旋排列为nxn的正方形矩阵matrix
'''

# 要点：对边的处理要遵循统一的规则，否则容易出现混淆。
# 比如在下面我们对处理的每条边遵循左闭右开的规则
from typing import List
class Solution:
    def generateMatrix(self,n:int)->List[List[int]]:
        nums_cycled = 0
        nums_cycle = n // 2
        start_x = 0
        start_y = 0
        offset = 1
        element = 1
        matrix =  [[0 for i in range(n)] for j in range(n)]
        # 考虑n=1的情况
        if n == 1:
            return [[1]]
        # 考虑n为奇数时最中间那个数
        if n>2 and n % 2 == 1:
            matrix[n//2][n//2] = n*n
        # 遍历多少圈
        while nums_cycled < nums_cycle:
            # 遍历最上边
            for y in range(start_x,n-offset):
                matrix[start_x][y] = element
                element += 1
            # 遍历最右边
            for x in range(start_y,n-offset):
                matrix[x][n-offset] = element
                element += 1
            # 遍历最下边
            for y in range(n-offset,start_y,-1):
                matrix[n-offset][y] = element
                element += 1
            # 遍历最左边
            for x in range(n-offset,start_x,-1):
                matrix[x][start_y] = element
                element += 1
            start_x += 1
            start_y += 1
            nums_cycled += 1
            offset += 1
        return matrix

if __name__ == "__main__":
    test = Solution()
    n = 3
    output = test.generateMatrix(n)
    print(output)        

