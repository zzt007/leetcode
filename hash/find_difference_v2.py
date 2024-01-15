# 对应leetcode 389

'''
    给定两个字符串s和t，只包含小写字母；
    字符串t由字符串s随机重排，然后在随机位置添加一个字母；
    要找到在t中被添加的字母。
'''
'''
    v2版本是修正v1版本的错误，v1版本在力扣测试时对很长的字符串输入报错，原因是x[0]说list index out of range。
    print了一下发现x是空列表，不懂为啥是空，x是代表在t中而不在s中的元素，如果是空，那不就代表s和t的key一样吗？那为什么还能运行到这？

    现使用列表实现哈希表，同时结合小写字母的ascii码进行编写,
    大致思路：
    1、小写字母a的ascii码数值为97，共有26个字母，为符合我们对下标的一般使用（从0开始），我们通过26个小写字母对应的ascii码数值相减来构建从0开始的小标，如0 = ascii(a)-ascii(a)，1 = ascii(b)-ascii(a)
    2、将下标当成是哈希表的key，将每个字母访问的次数当成是哈希表的value
    3、为避免设置和操作两个列表构建s、t各自的哈希表，我们在value层面上采用的策略是：对属于s字符串的字母，遍历后value -=1 ；对属于t字符串的字母，遍历后value +=1，由于t比s多一个字母，所以+1 和 -1低消后，value=1的即为多出来的
    4、找到value=1对应的key，并将key转回成对应的ascii数值再进一步转成小写字母
'''

class Solution:
    def __init__(self):
        self.hashtable = [0] * 26
    
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        
        for i in range(len(t)):
            if i < len(s):
                self.hashtable[ord(s[i])-ord('a')] -= 1
            self.hashtable[ord(t[i])-ord('a')] += 1

        for i in range(len(self.hashtable)):
            if self.hashtable[i] == 1:
                return chr(i+ord('a'))
            
if __name__ == "__main__":
    test = Solution()
    s = 'abcdefg'
    t = 'abbcdefg'
    output = test.findTheDifference(s, t)
    print(output)
            
# 还有针对此题更快的解法，即把字符串全部转成ascii码数值进行计算，两者做差即可
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in t:
            res = res + ord(i)
        for j in s:
            res -= ord(j)
        return chr(res)
'''