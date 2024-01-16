from .ListNode import ListNode
class SingleLinkedList:
    def __init__(self):
        self._head = None

    def isEmpty(self):
        return self._head is None
    
    def len(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        cur = self._head
        while cur is not None:
            yield cur.travel
            cur = cur.next

    def add(self, item):
        node = ListNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = ListNode(item)
        if self.isEmpty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        
    def insert(self,index,item):
        if index <= 0:
            self.add(item)
        elif index > self.len() - 1:
            self.append(item)
        else:
            node = ListNode(item)
            cur = self._head
            for _ in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def find(self,item):
        return item in self.travel()

