# coding=utf-8
'''
Created on 2017å¹?8æœ?20æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        ans = 1
        q = [root]

        while q:
            temp = []
            for node in q:
                temp.append(node.left if node else None)
                temp.append(node.right if node else None)
            i, j = 0, len(temp) - 1
            while i <= j and temp[i] == None: i += 1
            while i <= j and temp[j] == None: j -= 1
            temp = temp[i:j + 1]
            ans = max(len(temp), ans)
            q = temp
        return ans


root = list_to_tree([1, 3, 2, 5, 3, None, 9])
print Solution().widthOfBinaryTree(root)
