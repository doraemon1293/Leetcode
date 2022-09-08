# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = []

        def summ(node):
            if node == None:
                return (0, 0)
            l = summ(node.left)
            r = summ(node.right)
            res = l[0] + r[0] + node.val
            if res // (l[1] + r[1] + 1) == node.val:
                self.ans.append(node)
            return (res, l[1] + r[1] + 1)

        summ(root)
        return len(self.ans)
