# coding=utf-8
'''
Created on 2017å¹?5æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans = []

        def dfs(k, n, ans):  # put k-th row ans[i]=j mean i-row j-col is a queen
            possible = set(range(n))
            for x in range(len(ans)):
                possible.discard(ans[x])
                possible.discard(ans[x] + k - x)
                possible.discard(ans[x] - (k - x))
            for x in possible:
                ans.append(x)
                if k == n - 1:
                    temp = [["."] * n for _ in range(n)]
                    for x in range(n):
                        temp[x][ans[x]] = "Q"
                    self.ans.append(["".join(x) for x in temp])
                else:
                    dfs(k + 1, n, ans)
                ans.pop()

        dfs(0, n, [])
        return self.ans


print Solution().solveNQueens(4)
