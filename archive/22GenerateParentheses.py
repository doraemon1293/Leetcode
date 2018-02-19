# coding=utf-8
'''
Created on 2016�?11�?22�?

@author: Administrator
'''


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def dfs(left, right, s):
            if left == right == n:
                ans.append(s)
            if left < n:
                dfs(left + 1, right, s + "(")
            if right < left:
                dfs(left, right + 1, s + ")")

        dfs(0, 0, "")
        return ans


n = 3
print Solution().generateParenthesis(n)

