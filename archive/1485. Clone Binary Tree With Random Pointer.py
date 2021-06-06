# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
            self.val = val
            self.left = left
            self.right = right
            self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        d={None:None}
        def copy_tree(root):
            if root==None:
                return None
            left=copy_tree(root.left)
            right=copy_tree(root.right)
            node=NodeCopy(val=root.val,left=left,right=right,random=root.random)
            d[root]=node
            return node
        def inorder(root):
            if root:
                root.random=d[root.random]
                inorder(root.left)
                inorder(root.right)
        root=copy_tree(root)
        inorder(root)
        return root


