# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parents={}
        def inorder(node,parent):
            if node:
                inorder(node.left,node)
                parents[node]=parent
                inorder(node.right,node)
        inorder(root,None)
        if p not in parents or q not in parents:
            return None
        parents_p=set()
        node=p
        while node:
            parents_p.add(node)
            node=parents[node]
        node=q
        while node:
            if node in parents_p:
                return node
            node=parents[node]
        

