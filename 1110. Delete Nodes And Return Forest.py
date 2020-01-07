# Definition for a binary tree node.

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        self.ans = []
        self.q = collections.deque()
        self.q.append((root, None))

        def pre(root, parent):
            if root != None:
                if root.val in to_delete:
                    if parent:
                        if parent.left == root:
                            parent.left = None
                        if parent.right == root:
                            parent.right = None
                    self.q.append((root.left,None))
                    self.q.append((root.right,None))
                else:
                    pre(root.left, root)
                    pre(root.right, root)

        while self.q:
            root, parent = self.q.popleft()
            if root and root.val not in to_delete:
                self.ans.append(root)
            pre(root, parent)

        return self.ans
