# 对应leetcode 705

'''
    不适用任何内建的哈希表库设计一个哈希集合，实现如下功能
    add(value):向哈希集合中插入一个值
    contains(value):返回哈希集合中是否存在这个值
    remove(value):将给定值从哈希集合中删除，若无该值，则不进行任何操作

    如果要使用数组的方法，一般需要提前告知空间大小，否则一般无法使用数组。
    这里是写了所有值都在[0,1000000]范围内；用数组实现，相当于用空间复杂度换取时间复杂度，设计一个这么大的布尔类型的数组，下标对应值，value对应true 1 or false 0

'''

class MyHashSet:
    def __init__(self):
        self.nums = [0] * 1000001

    def add(self,value:int):
        self.nums[value] = 1

    def remove(self,value:int):
        self.nums[value] = 0

    def contains(self,value:int)->bool:
        return self.nums[value]
    
# 优秀解法
class MyHashSet:

    def __init__(self):
        self.s = set()


    def add(self, key: int) -> None:
        self.s.add(key)


    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)


    def contains(self, key: int) -> bool:
        if key in self.s:
            return True
        else:
            return False

    
