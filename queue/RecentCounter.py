# 对应leetcode 933
'''
    写一个RecentCounter类来计算特定时间范围内发起请求的次数
    RecentCounter（）初始化计数器，请求数为0
    int ping(int t)在时间t添加一个新请求，其实t表示以毫秒为单位的某个时间
    并返回过去3000ms内发生的所有请求数
'''
# 创建队列时，可以使用python collections模块的deque，也可以自己实现一个类，里面包含一些队列的常用方法

import time
import collections

class RecentCounter:
    def __init__(self) -> None:
        count = 0
        queue = collections.deque()
        self.count = count 
        self.queue = queue

    def ping(self,t:int)->int:
        self.queue.append(t)
        if len(self.queue) != 0:
            while t - self.queue[0] > 3000:
                self.queue.popleft()
        self.count = len(self.queue)
        print(self.count)
        print(self.queue)
        return self.count
    
if __name__ == '__main__':
    test = RecentCounter()
    test.ping(100)
    test.ping(3000)
    test.ping(3001)
    test.ping(4001)

'''
    小结：deque（）是创建双端队列，其操作和列表很像
    需要注意删除的逻辑，因为这里的计数逻辑要基于边删除头元素来计数
'''
