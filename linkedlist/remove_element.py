# 对应习题203
# 2024-01-23 重温链表

# 使用dummy节点辅助完成
class LinkedListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
    
    def print_valandnext(self):
        print(self.val)
        print(self.next)


class Solution:
    def removeElements(self,head:LinkedListNode,target:int):
        # 首先定义一个dummy节点
        dummy = LinkedListNode(-100)
        dummy.next = head
        cur = dummy # 为什么要让一个临时指针等于dummy，而不是等于dummy.next，因为在删除链表元素的过程中，我们需要知道该元素的前驱元素，进而才能cur.next = cur.next.next
        cur.next.print_valandnext
        while cur != None and cur.next != None:
            cur.print_valandnext()
            if cur.next.val == target:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

if __name__ == "__main__":
    test = Solution()
    head = LinkedListNode(1)
    node1 = LinkedListNode(2)
    node2 = LinkedListNode(3)
    node3 = LinkedListNode(4)

    head.next = node1
    node1.next = node2
    node2.next = node3

    output = test.removeElements(head,2)
    print(output)
