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
        print(self.minheap)
        
        res = []
        self.minheap = sorted(self.minheap,key= lambda x:(-x[0],x[1]))
        print(self.minheap)
        for i in range(k):
            res.append(self.minheap[i][1])
        # print(res)
        return res
    
if __name__ == "__main__":
    test = Solution()
    words =["the","day","is","sunny","the","the","the","sunny","is","is"]
    k = 4
    print(test.findKFrequenceWord(words,k))


# 关于lambda表达式和sort与lambda合用的，可以参考如下两篇
# https://blog.csdn.net/qq_41500249/article/details/106244810
# https://blog.csdn.net/PY0312/article/details/88956795
    

# 优秀解法，不需要hashtable进行元素统计，直接利用collections模块自带的counter
# 用法参考：https://blog.csdn.net/chl183/article/details/106956807
from collections import Counter # 可以快速进行元素统计，返回一个字典，键为元素，值为个数
class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]