# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def foo(node, nums):
            if node != None:
                nums.append(node.val)
                if node.left == None and node.right == None:
                    self.ans += int("".join([str(x) for x in nums]))
                if node.left:
                    foo(node.left, nums)
                if node.right:
                    foo(node.right, nums)
                nums.pop()

        foo(root, [])
        return self.ans


root = TreeNode(0)
print Solution().sumNumbers(root)
