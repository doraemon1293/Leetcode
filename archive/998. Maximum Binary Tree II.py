# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def deconstruct(root):
            if root:
                return deconstruct(root.left) + [root.val] + deconstruct(root.right)
            else:
                return []

        def construct(arr):
            if arr == []:
                return None
            maxi = -float("inf")
            for i, x in enumerate(arr):
                if x > maxi:
                    maxi = x
                    max_ind = i
            root = TreeNode(maxi)
            root.left = construct(arr[:i])
            root.right = construct(arr[i + 1:])
            return root

        b = deconstruct(root) + [val]
        print(b)
        return construct(b)
