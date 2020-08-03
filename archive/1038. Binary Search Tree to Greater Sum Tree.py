# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root):
        self.sum=0
        arr=[]
        def succ(root):
            if root!=None:
                succ(root.right)
                self.sum+=root.val
                root.val=self.sum
                succ(root.left)
        succ(root)
        return root



