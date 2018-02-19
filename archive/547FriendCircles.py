# coding=utf-8
'''
Created on 2017å¹?5æœ?9æ—?

@author: Administrator
'''


class Solution(object):

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # ä¼ é?’é—­åŒ…æ–¹æ³? -- æ¯”dfsæ…?
#         for k in range(len(M)):
#             for i in range(len(M)):
#                 for j in range(len(M)):
#                     if M[i][j] != 1:
#                         M[i][j] = M[i][j] or M[i][k] and M[k][j]
#         ans = 0
#         s = set(range(len(M)))
#         i = 0
#         for i in range(len(M)):
#             if i in s:
#                 s.remove(i)
#                 ans += 1
#                 for j in range(len(M)):
#                     if M[i][j]:
#                         s.discard(j)
#         return ans

        # DFS
        self.s = set(range(len(M)))

        def dfs(n):
            for i in range(len(M)):
                if M[n][i] and i in self.s:
                    self.s.discard(i)
                    dfs(i)

        ans = 0
        for i in range(len(M)):
            if i in self.s:
                ans += 1
                self.s.discard(i)
                dfs(i)
        return ans

