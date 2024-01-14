# 使用python实现队列结构
# 参考：https://blog.csdn.net/qq_39611230/article/details/103080386

'''
主要实现如下功能：(单端队列)
1、往队列头中添加一个新元素
2、遍历所有元素
3、从队列尾删除一个元素
4、判断队列是否为空
5、返回队列的元素个数（即队列长度）
'''

class Queue:
    def __init__(self):
        self.__data = []

    def enqueue(self,data):
        # 往队列头中添加一个新元素
        self.__data.insert(0,data)

    def travel(self):
        # 遍历所有元素
        for i in self.__data:
            print(i,end='')
        print('')

    def dequeue(self):
        # 从队列尾删除一个元素
        if self.is_empty():
            print("队列为空，无法删除元素")
            return None
        return self.__data.pop()

    def is_empty(self):
        # 判断队列是否为空
        return self.__data == []
    
    def len(self):
        # 返回队列长度
        return len(self.__data)