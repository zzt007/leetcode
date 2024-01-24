# 对应习题349，难度为简单
'''
    给定两个数组nums1和nums2，返回它们的交集。
    输出结果中的每个元素一定是唯一的，可以不考虑输出结果的顺序。
'''

from typing import List
class Solution:
    def intersection(self,nums1:List[int],nums2:List[int]) -> List[int]:
        # 定义一个hash表，用字典实现
        hash = {}
        # 定义一个空列表用于存放结果
        res = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for num in nums1:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        for num in nums2:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        # 遍历哈希表，如果value>= 2，则返回对应的key
        for key,value in hash.items():
            if value >= 2:
                res.append(key)
        return res

# 其实上面是比较笨的写法，不仅使用了哈希表统计两个数组，还对数组提前使用了set去重
# 还可以用不用哈希，就遍历一个数组，看它的元素是否在另一个数组中，如果在，则该元素为交集元素，否则不是。但是好像还是要去重
class Solution_v2:
    def intersection(self,nums1,nums2):
        res = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
        return set(res) 




if __name__ == "__main__":
    test = Solution_v2()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    output = test.intersection(nums1,nums2)
    print(output)
