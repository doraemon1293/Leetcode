# coding=utf-8
'''
Created on 2017å¹?6æœ?18æ—?

@author: Administrator
'''
from collections import deque

from data_structure.Tree import list_to_tree, tree_to_list


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """

        def levelTraverseFromRoot(root):
            ans = []
            if root:
                current_level = 0
                q = deque()
                q.append((root, 0))
                temp = []
                while q:
                    node, level = q.popleft()
                    if level > current_level:
                        ans.append(temp)
                        temp = []
                        current_level += 1
                    temp.append(node)
                    if node.left:
                        q.append((node.left, current_level + 1))
                    if node.right:
                        q.append((node.right, current_level + 1))
                ans.append(temp)
            return ans

        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        level_order = levelTraverseFromRoot(root)
        level_order = level_order[d - 2]

        for node in level_order:
            temp = node.left
            node.left = TreeNode(v)
            node.left.left = temp
            temp = node.right
            node.right = TreeNode(v)
            node.right.right = temp
        return root


root = list_to_tree([4, 2, 6, 3, 1, 5])
v = 1
d = 2
ans = Solution().addOneRow(root, v, d)
print tree_to_list(ans)
