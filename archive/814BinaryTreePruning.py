# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def hasone(node):
            if node==None:
                return False
            if node.val:
                return True
            else:
                if hasone(node.left) or hasone(node.right):
                    return True

        def prune(root):
            if not hasone(root):
                return None
            else:
                if not hasone(root.left):
                    root.left=None
                else:
                    prune(root.left)
                if not hasone(root.right):
                    root.right=None
                else:
                    prune(root.right)
            return root
        return prune(root)


