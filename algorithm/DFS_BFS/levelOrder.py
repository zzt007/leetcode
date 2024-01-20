# 对应习题102
'''
    层序遍历一个二叉树，并返回每一层的节点值
'''

# 使用BFS解决,BFS总是和队列联系在一起
from collections import deque
from typing import List
# from ...tree import createBinTree,TreeNode
class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

# 定义二叉树
class BinTree:
    def __init__(self):
        self.root = None # 定义根节点
        self.address_list = [] # 定义用于存储节点地址的列表

    # 实现向树中添加节点的功能
    def add(self,data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            self.address_list.append(self.root)
        else:
            rootNode = self.address_list[0]
            if rootNode.left == None:
                rootNode.left = node
                self.address_list.append(rootNode.left)
            elif rootNode.right == None:
                rootNode.right = node
                self.address_list.append(rootNode.right)
                self.address_list.pop(0) # 为什么要pop掉root节点的地址？因为这里构建的是完全二叉树，每次add都跟着一个新的节点来生成左右孩子节点
    
    def preOrderTravel(self,root):
        if root == None:
            return
        print(root.data)
        self.preOrderTravel(root.left)
        self.preOrderTravel(root.right)

class Solution:
    def levelOrder(self,root:TreeNode)->List[List[int]]:
        res = []
        if root is None:
            return res
        queue = deque([])
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            ls = []
            while size > 0:
                cur = queue.popleft()
                ls.append(cur.data)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                size -= 1
            res.append(ls[:])

        return res
if __name__ == "__main__":
    test = Solution()
    # 创建demo树
    mytree = BinTree()
    for i in range(1,11):
        mytree.add(i)
    # mytree.preOrderTravel(mytree.root)
    output = test.levelOrder(mytree.root)
    print(output)

