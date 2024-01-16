# 对应leetcode 141
'''
    给定一个链表，判断链表中是否存在环，存在则返回True，否则为False。
'''

# import sys
# sys.path.append(r"D:\leetcode\leetcode\linkedlist")
# import ListNode

# 使用相对位置进行导入
# from ...linkedlist import ListNode

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val 
        self.next = next

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        slow = head
        fast = head
        # 疑问：快慢指针的初始位置有要求嘛？
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

test = Solution()
print(test.hasCycle(node1))