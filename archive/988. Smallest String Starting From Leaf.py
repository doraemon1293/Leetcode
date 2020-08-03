# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        self.leaves = []

        def dfs(root):
            if root.left:
                root.left.p = root
                dfs(root.left)
            if root.right:
                root.right.p = root
                dfs(root.right)
            if root.left == root.right == None:
                self.leaves.append(root)

        dfs(root)
        leaves = self.leaves
        ans = []
        while root not in leaves:
            mini = min([leaf.val for leaf in leaves])
            ans.append(mini)
            leaves = [leaf.p for leaf in leaves if leaf.val == mini]
            print([leaf.val for leaf in leaves])
        ans.append(root.val)

        return "".join([chr(x+ord('a')) for x in ans])
