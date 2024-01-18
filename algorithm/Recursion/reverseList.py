# 对应习题206
'''
    给定一个单端链表，将其反转后输出
'''

class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self,head:ListNode)->ListNode:
        if head is None or head.next is None:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res

if __name__ == '__main__':
    test = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    output = test.reverseList(head)
    print(output,output.next)