# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        self.nodes={}
        def dfs(root,parent,depth):
            if root:
                self.nodes[root.val]=(parent,depth,)
                dfs(root.left,root.val,depth+1)
                dfs(root.right,root.val,depth+1)
        dfs(root,None,0)
        parent_x,depth_x=self.nodes[x]
        parent_y,depth_y=self.nodes[y]
        return depth_x==depth_y and parent_x!=parent_y

