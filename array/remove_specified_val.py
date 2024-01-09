# 对应leetcode 27
'''
    给定一个数组和一个指定值，需要在原始数组元素中等于指定值的元素移除，并返回移除后的数组长度
    元素的顺序可以改变，不需要考虑数组中超出新长度后的元素
'''

# 经典错误
# input = [3,2,2,3,3,3,1,4,5,6,7,2]
# specified_value = 2
# for num in input:
#     if num == specified_value:
#         input.remove(num)
# print(len(input))
# print(input)

# 和我一样的经典错误，for循环中利用remove删除list元素：
# https://www.jianshu.com/p/e20c78153299 和 https://zhuanlan.zhihu.com/p/413921093
'''
    原因分析：在使用for对数组进行循环时，按照下标从0开始循环，对于数组所占用的一块连续存储空间，
    每当使用remove指令删去一个元素时，后面的元素会自动往前，即相当于后面元素的下标-1，但是由于for循环
    已经循环过了同样的下标，就会继续往下，导致跳过一个同样的val
'''

# 可以采用双指针算法完成
from typing import List
class Solution:
    def remove_specified_val(self,nums:List[int],val:int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        l , r = 0, len(nums)-1
        while l<r:
            while (l<r and nums[l] != val):
                l += 1
            while (l<r and nums[r] == val):
                r -= 1
            nums[l],nums[r] = nums[r],nums[l]
        return l if nums[l] == val else l+1

if __name__ == '__main__':
    solution = Solution()
    input = [3,2,2,3,3,3,1,4,5,6,7,2]
    specified_value = 3
    output = solution.remove_specified_val(input,specified_value)
    print(output)



