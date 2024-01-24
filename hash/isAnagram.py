# 对应习题242
'''
    给定两个字符串s和t，编写一个函数来判断t是否是s的字母异位词
    异位词定义：当s和t中每个字符出现的次数都相同，则称s和t互为字母异位词
'''

# 这里比较巧妙的是，我们可以使用数组来实现哈希表
# key为数组的下标，value为字符出现次数
# 那怎么让key刚好满足数组下标从0开始的顺序呢，可以使用ascii码

from typing import List
class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        # 创建一个初始值全为0的，长度为26的数组
        hash = [0]*26
        # 遍历s中的每个字符并计数
        for i in s:
            hash[ord(i)-ord('a')] += 1
        for j in t:
            hash[ord(j)-ord('a')] -= 1
        # 一加一减，可以知道是哪个字符串多了哪个字符
        for k in range(len(hash)):
            print(hash)
            if hash[k] != 0:
                return False
        return True
            
if __name__ == "__main__":
    test = Solution()
    s = "rat"
    t = "car" 
    output = test.isAnagram(s,t)
    print(output)               
        