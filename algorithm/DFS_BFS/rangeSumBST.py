# 对应习题938
'''
    给定二叉搜索树的根节点root，返回值位于范围[low,high]之间的所有节点的值之和
'''

# 递归、BFS\DFS都可以
# 递归是对左子树、右子树和根节点求和（需要判断节点值是否满足范围）


# 导入树结构
from ...tree import createBinTree,TreeNode
# 导入队列
import collections
# BFS，一层一层地遍历求和，需要使用一个队列来存储用于计算的节点值
class Solution_BFS:
    def rangeSumBST(self, root:TreeNode,low:int,high:int):
        res = 0
        queue = collections.deque()
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                cur = queue.pop()
                if cur.val >= low and cur.val <= high:
                    res = res + cur.val
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                size = size - 1
        return res

# DFS，记当前子树根节点为root，分4种情况讨论
'''
    (1)root节点为空、(2)root节点值大于high、(3)root节点值小于low、(4)root节点值在[low,high]内
    这里用到了二叉搜索树的性质：
    1、若左子树非空，则左子树上的所有节点的值小于根节点的值
    2、若右子树非空，则右子树上的所有节点的值大于根节点的值
    3、左、右子树本身也分别是一棵二叉搜索树

    所以，第(1)种情况返回0，（2）返回左子树范围和，（3）返回右子树范围和，（4）返回root节点值+左右子树范围和
'''

class Solution_DFS:
    def rangeSumBST(self,root:TreeNode,low:int,high:int)->int:
        if not root:
            return 0 
        if root.val > high:
            return self.rangeSumBST(root.left,low,high)
        if root.val < low:
            return self.rangeSumBST(root.right,low,high)
        return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)

    

