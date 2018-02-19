# coding=utf-8
'''
Created on 2017å¹?6æœ?14æ—?

@author: Administrator
'''
from test.test_iterlen import NoneLengthHint
import re

from data_structure.Tree import tree_to_list


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """

        def foo(s):
            if s == "": return None
            l_s, l_e = None, None
            r_s, r_e = None, None
            parathesis = 0
            for i, c in enumerate(s):
                if c == "(":
                    if parathesis == 0:
                        if l_s == None:
                            l_s = i + 1
                        else:
                            r_s = i + 1
                    parathesis += 1
                if c == ")":
                    parathesis -= 1
                    if parathesis == 0:
                        if l_e == None:
                            l_e = i - 1
                        else:
                            r_e = i - 1
            num = int(s[:l_s - 1]) if l_s != None else int(s)
            node = TreeNode(num)
            if l_s != None: node.left = foo(s[l_s:l_e + 1])
            if r_s != None: node.right = foo(s[r_s:r_e + 1])
            return node

        return foo(s)


s = "4(2(3)(1))(6(5)(7))"
root = Solution().str2tree(s)
print tree_to_list(root)

