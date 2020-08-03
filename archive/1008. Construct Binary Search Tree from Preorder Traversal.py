# Definition for a binary tree node.
import bisect


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def construct(arr):
            if arr:
                val = arr[0]
                root = TreeNode(val)
                ind = bisect.bisect(arr, val)
                root.left = construct(arr[1:ind])
                root.right = construct(arr[ind:])
                return root
            else:
                return None
        return construct(preorder)