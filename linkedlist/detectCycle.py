# 对应习题142
'''
    给定一个链表的头节点head，返回链表开始入环的第一个节点。
    如果链表无环，则返回NULL

    这题是判断链表有无环的进阶版，还需要给出入环的节点
    这里判断环入口的方式是需要先找到相遇点的，然后在head和相遇点处各设一个指针，当指针相遇时即为环入口
'''

# 快慢指针
from .ListNode import ListNode
class Solution:
    def detectCycle(self,head:ListNode) -> listNode:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next

            if slow == fast:
                # 即已相遇，然后下面让slow在head处重新开始，就省去了多定义一个变量
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            return None