from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.lonelynodes=[]
        def inorder(node):
            if node:
                if node.left:
                    if node.right==None:
                        self.lonelynodes.append(node.left.val)
                    inorder(node.left)
                if node.right:
                    if node.left==None:
                        self.lonelynodes.append(node.right.val)
                    inorder(node.right)
        inorder(root)
        return self.lonelynodes