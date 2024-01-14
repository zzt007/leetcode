# 对应leetcode 20
'''
    给定一个只包括'(',')','{','}' ,'[',']'的字符串，判断字符串是否有效
    有效的定义是：左括号必须用相同类型的右括号闭合、且以正确的顺序闭合   
'''

'''
使用stack来实现，遍历字符串，当为左括号时，将其压入栈；
当为右括号时，将其与栈顶元素对比，是否为同类型，是则返回有效，否则无效
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif c == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif c== ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                elif c == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

# test
if __name__ == '__main__':
    test = Solution()
    s = "()(){{    } }"
    output = test.isValid(s)
    print(output)

'''
    小结：这种可以明显分成两类进行对比的数据且还有顺序或者是特殊要求的，可以使用栈来解决

'''