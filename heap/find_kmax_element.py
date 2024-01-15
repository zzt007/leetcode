# 对应leetcode 215

'''
    在未排序的数组中找到第k个最大的元素。
    通俗讲，找到一个无序数组里的第几大的元素
'''

# 用最大堆实现,可以使用python自带的heapq模块实现最小堆，再对最小堆取反得到最大堆
import heapq
from typing import List
class Solution:
    def __init__(self) -> None:
        self.heap = []

    def findKthLargest(self, nums: List[int], k: int) -> int:
        for num in nums:
            heapq.heappush(self.heap, -num)
        print(type(self.heap))
        print(self.heap)
        print('len is: ',len(self.heap))
        if len(self.heap) < k:
            return -self.heap[0]
        for _ in range(k-1):
            heapq.heappop(self.heap)
        print(self.heap)
        return -self.heap[0]

if __name__ == '__main__':
    test = Solution()
    nums = [3,2,1,-1,-2,-3]
    k = 2
    output = test.findKthLargest(nums, k)
    print(output)
