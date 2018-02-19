# coding=utf-8
'''
Created on 2017å¹?7æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if preorder == []: return True
        stack = [preorder[0]]
        low = -float("inf")
        for num in preorder[1:]:
            if num < stack[-1]:
                if num < low: return False
                stack.append(num)
            else:
                while stack and num > stack[-1]:
                    low = stack.pop()
                if stack and num > stack[-1]: return False
                stack.append(num)
        return True


preorder = [2, 3, 1]
print Solution().verifyPreorder(preorder)
