# 创建二叉树，并且实现前序遍历
# 参考：https://blog.csdn.net/Tonywu2018/article/details/89480282

'''
    此处采用链式存储结构实现二叉树，因为对于顺序存储结构实现二叉树来说，用数组实现，但是只有完全二叉树才能使用顺序存储
    一般二叉树结构也可以转换成完全二叉树后再进行顺序存储
    常用的针对一般二叉树的实现使用链式存储，用链表实现
'''

# 定义树的节点
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


if __name__ == "__main__":
    tree = BinTree()
    for i in range(1,11):
        tree.add(i)
    tree.preOrderTravel(tree.root)
    

