# coding=utf-8
'''
Created on 2017å¹?5æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.ans = 0

        def dfs(k, n, ans):  # put k-th row ans[i]=j mean i-row j-col is a queen
            possible = set(range(n))
            for x in range(len(ans)):
                possible.discard(ans[x])
                possible.discard(ans[x] + k - x)
                possible.discard(ans[x] - (k - x))
            for x in possible:
                ans.append(x)
                if k == n - 1:
                    self.ans += 1
                else:
                    dfs(k + 1, n, ans)
                ans.pop()

        dfs(0, n, [])
        return self.ans
