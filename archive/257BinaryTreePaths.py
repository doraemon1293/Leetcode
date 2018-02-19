# coding=utf-8
'''
Created on 2016å¹?11æœ?9æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        ans = []

        def dfs(node, path):
            if node.left == None and node.right == None:
                path = path + [node.val]
                ans.append("->".join(str(x) for x in path))
            else:
                path = path + [node.val]
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)

        if root:
            dfs(root, [])
        return ans
