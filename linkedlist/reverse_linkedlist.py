# 对应leetcode 206
'''
    给定一个单端链表，需要将链表中的元素顺序反过来排序，输出反序的链表
    例： input为 1->2->3->4 , output为 4->3->2->1
'''

from linkedlist import ListNode
class Solution:
    def reverseLinkedlist(self,head:ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head # 先初始化dummy和head之间的连接关系，即dummy的next指向是head
        while head is not None and head.next is not None:
            dnext = dummy.next # 定义dnext和hnext，用于辅助后续顺序调换
            hnext = head.next
            dummy.next = hnext # 实际上就是dummy.next = head.next，这里就是把dummy链接的下一个元素从head替换成了head.next
            head.next = hnext.next # 上一句调换地址链接顺序后，现将head和head.next值进行调换
            hnext.next = dnext
        return dummy.next

# 小结：dummy作为一个虚拟结点，最后返回dummy.next，其实有点句柄的感觉