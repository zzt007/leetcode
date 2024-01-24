# 对应习题454，难度为中等
'''
    给定四个整数数组nums1到nums4，数组长度都是n，计算有多少个元素[i,j,k,l]能满足对应元素之和=0
    即不需要返回是哪四个元素之和等于0，只需要返回有多少组这样的四元素
'''

# 如果是暴力直接4个for循环，时间复杂度为O(n四次方)
# 所以可以把4个数组分成两个2数组循环，变成O(n²) + O(n²)
from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash = {}
        for n1 in nums1:
            for n2 in nums2:
                if nums1[n1] + nums2[n2] in hash:
                    hash[n1+n2] += 1
                else:
                    hash[n1+n2] = 1
        # 计算有多少组四元素
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                # 也是和之前两数之和一样，利用目标值和差值之间的关系来查找已存在hash表里的元素
                target = 0-n3-n4
                # 并不是count += 1，因为哈希表里存储的是n1+n2的多种可能
                if target in hash:
                    count += hash[target]
        return count