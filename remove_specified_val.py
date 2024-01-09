# 对应leetcode 27
'''
    给定一个数组和一个指定值，需要在原始数组元素中等于指定值的元素移除，并返回移除后的数组长度
    元素的顺序可以改变，不需要考虑数组中超出新长度后的元素
'''

# 经典错误
input = [3,2,2,3,3,3,1,4,5,6,7,2]
specified_value = 2
for num in input:
    if num == specified_value:
        input.remove(num)
print(len(input))
print(input)

# 和我一样的经典错误，for循环中利用remove删除list元素：
# https://www.jianshu.com/p/e20c78153299 和 https://zhuanlan.zhihu.com/p/413921093

# 可以采用双指针算法完成

