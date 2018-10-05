# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leafofroot(root):
            if root.left==root.right==None:
                return [root.val]
            res=[]
            if root.left:
                res+=leafofroot(root.left)
            if root.right:
                res+=leafofroot(root.right)
            return res
        #print(leafofroot(root1),leafofroot(root2))
        return leafofroot(root1)==leafofroot(root2)

print(Solution().leafSimilar(rot))


