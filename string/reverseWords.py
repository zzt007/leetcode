# 对应习题151
'''
    给定一个字符串s，反转字符串中单词的顺序。
    s中使用至少一个空格将字符串中的单词隔开。
'''

class Solution:
    def reverseWords(self,s:str) -> str:
        # 使用strip（）方法删除开头和结尾的指定字符（可以是空格），不能删除中间部分的
        s = s.strip()
        # 反转整个字符串
        s = s[::-1]
        # 将字符串拆分为单词，并反转每个单词
        s = ' '.join(word[::-1] for word in s.split())
        return s
    
    def reverseWords_v2(self,s:str) -> str:
        words = s.split()
        print(type(words))
        print(words)
        # 双指针反转
        left , right = 0,len(words)-1
        while left < right:
            words[left],words[right] = words[right],words[left]
            left += 1
            right -= 1
        return " ".join(words)

if __name__ == "__main__":
    test = Solution()
    s = " the sky is blue "
    output = test.reverseWords(s)
    print(output)


# 小结：用py编写由于字符串是不可变类型，所以必须得超过O(1)空间复杂度
# 方法1的思路：先全部反转，再对每个单词反转
# 方法2的思路：先把字符串转成列表，然后对列表元素使用双指针来交换位置
    