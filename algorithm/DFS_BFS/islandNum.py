# 对应习题200
'''
    给定一个由'1'(陆地)和'0'(水)组成的二维网格，计算网格中岛屿的数量
    岛屿只能由水平或垂直方向上相邻的陆地连接而成
'''

# 使用DFS解决，目标是：遍历找到1，然后同化相邻的1变成0，计数器+1
from typing import List
# class Solution_DFS:
#     def numIslands(self,grid:List[List[int]])->int:
#         if len(grid) == 0 or grid is None:
#             return 0
#         res = 0
#         row = len(grid)
#         col = len(grid[0])
#         # 按grid的行和列逐个遍历
#         for i in range(0,row):
#             for j in range(0,col):
#                 if grid[i][j] == 1:
#                     res += 1
#                     self.set_1_to_0(grid,row,col,i,j)
#         return res
    
#     def set_1_to_0(self,grid,row,col,i,j):
#         if i < 0 or j<0 or i>= row or j>= col or grid[i][j] == 0:
#             return
#         # 先把找到的1变为0
#         grid[i][j] = 0
#         # 对找到的‘1’相邻区域（上下左右）进行递归搜索，但是我感觉其实只要搜索下和右就行了，因为找1时的顺序就是一个一个来的
#         # self.set_1_to_0(grid,row,col,i-1,j)
#         self.set_1_to_0(grid,row,col,i+1,j)
#         # self.set_1_to_0(grid,row,col,i,j-1)
#         self.set_1_to_0(grid,row,col,i,j+1)

import collections
# 使用BFS时，通常都会需要一个队列来辅助，用于存储将要处理的值
class Solution_BFS:
    def numIslands(self,grid:List[List[int]])->int:
        if grid is None or len(grid) == 0:
            return 0
        res = 0
        queue = []
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res += 1
                    queue.append([i,j])
                    grid[i][j] == 0
                    self.set_1_to_0(grid,queue,row,col)
        return res 

    def set_1_to_0(self,grid,queue,row,col):
        while len(queue) > 0:
            temp = queue.pop()
            x = temp[0]
            y = temp[1]
            if x+1 < row and grid[x+1][y] == 1:
                queue.append([x+1,y])
                grid[x+1][y] = 0
            if y+1 < col and grid[x][y+1] == 1:
                queue.append([x,y+1])
                grid[x][y+1] = 0
            




if __name__ == "__main__":
    test = Solution_BFS()
    # grid = [['0','1','1'],['0','1','0'],['0','0','0']]
    grid = [[0, 1, 1], [0, 1, 0], [0, 0, 0]]
    output = test.numIslands(grid)
    print(grid)
    print(output)

# 视频中还介绍了使用并查集解决该题
# 关于并查集，可以参考：https://blog.csdn.net/the_ZED/article/details/105126583?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522170573285116800182170403%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=170573285116800182170403&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-105126583-null-null.142^v99^pc_search_result_base7&utm_term=%E5%B9%B6%E6%9F%A5%E9%9B%86&spm=1018.2226.3001.4187