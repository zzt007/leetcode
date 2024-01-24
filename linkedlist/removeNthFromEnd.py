# 对应习题19，中等难度
'''
    给定一个链表，删除链表的倒数第n个节点，并返回链表的头节点
'''

# 对于链表删除元素而言，是需要知道被删除元素的前驱元素的，所以这道题就可以分解成两步
# 1、怎么表示出倒数元素
# 2、怎么找到元素的前驱元素
# 我们不妨采用快慢指针来表示，快指针走到NULL时即停，那可以通过比慢指针多走n步，进而当快指针为NULL时，慢指针恰好对应删除元素
# 为了能够删除指定的元素，我们让快指针先走n+1步，这样当快指针为NULL时，慢指针恰好对应删除元素的前驱元素

# 创建链表节点
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self,head:ListNode,n:int)->ListNode:
        dummy_head = ListNode(0,head)
        # 创建快慢指针，初始化为虚拟节点. 
        '''
            为什么不初始化为head节点呢?原因是当要删除head节点时，如果我们此时slow和fast都在head的位置，会有两个问题：一是由于快指针要先走n+1步，此时早已为空，会报空指针错误；二是slow并不在删除元素的前驱元素上
            为了统一化对链表元素的操作，都初始化为虚拟节点，这也是虚拟节点提出来的意义，不会因为头节点的特殊而需要另外对算法进行扩展或补充
        '''
        fast = dummy_head
        slow = dummy_head
        # 快指针先走n+1步
        for i in range(n+1):
            fast = fast.next
        # 同时移动快慢指针，直至快指针为None
        while(fast != None):
            fast = fast.next
            slow = slow.next
        # 此时慢指针对应删除元素的前驱元素,执行删除操作
        slow.next = slow.next.next值进行调换

        return dummy_head.next