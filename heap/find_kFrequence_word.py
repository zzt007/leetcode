# 对应leetcode 692

'''
    给一非空的单词列表，返回出现次数前k多的单词
    返回的答案按单词从出现频率高到低排序。如果频率一样，按字母顺序排。
'''

# 用最小堆 + 哈希表实现
from typing import List
import heapq

class Solution:
    def __init__(self) -> None:
        self.hashtable = {}
        self.minheap = []

    def findKFrequenceWord(self,words:List[str],k:int)->List[str]:
        for word in words:
            if word not in self.hashtable:
                self.hashtable[word] = 0
            self.hashtable[word] += 1
        # print(self.hashtable)
        for word in self.hashtable:
            heapq.heappush(self.minheap,(self.hashtable[word],word))
            if len(self.minheap) > k:
                heapq.heappop(self.minheap)
        
        res = []
        while len(self.minheap) > 0:
            temp = heapq.heappop(self.minheap)
            print(temp) # (1,'coding')
            res.append(temp[1])
            
        res.reverse()
        return res
    
if __name__ == "__main__":
    test = Solution()
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    print(test.findKFrequenceWord(words,k))