# coding=utf-8
'''
Created on 2017å¹?7æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(",")
        if preorder == []: return False
        if preorder[0] == "#" and len(preorder) == 1: return True
        if preorder[0] == "#" and len(preorder) > 1: return False
        stack = [preorder[0], preorder[0]]
        for s in preorder[1:]:
            if s == "#":
                if stack:
                    stack.pop()
                else:
                    return False
            else:
                if stack:
                    stack.pop()
                else:
                    return False
                stack.append(s)
                stack.append(s)
        return stack == []


preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
preorder = "1,#"

print Solution().isValidSerialization(preorder)
