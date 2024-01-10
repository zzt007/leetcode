# 对应leetcode 203
'''
    给定一个链表和指定值，需要移除链表中的指定值，返回链表
'''

from linkedlist import ListNode
# 创建链表
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

'''
    小结：在处理链表类的问题时，可以采用dummy变量，作为一个虚拟的链表节点
    可以消除链表头节点的特殊性，让它可以当成普通节点一样，因为很多涉及链表元素的操作
    都要用到上一节点的信息
'''
class Solution:
    def removeElements(self,head:ListNode,val:int) -> ListNode:
        dummy = ListNode(0) # dummy的值通常设为一些特殊值
        dummy.next = head
        prev = dummy # prev说previous的简称，代表前一个节点
        while head is not None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next
