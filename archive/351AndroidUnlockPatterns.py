# coding=utf-8
'''
Created on 2017å¹?5æœ?18æ—?

@author: Administrator
'''


class Solution(object):

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = {
           (2, 2):(1, 1), (2, -2):(1, -1), (-2, -2):(-1, -1), (-2, 2):(-1, 1),
           (2, 0):(1, 0), (-2, 0):(-1, 0), (0, 2):(0, 1), (0, -2):(0, -1)
           }
        self.ans = 0

        def dfs(p):
            if m <= len(p) <= n:
                self.ans += 1
            if len(p) < n:
                x, y = (p[-1] - 1) / 3, (p[-1] - 1) % 3
                for num in range(1, 10):
                    if num not in p:
                        x1, y1 = (num - 1) / 3, (num - 1) % 3
                        x0, y0 = d.get((x1 - x, y1 - y), (None, None))
                        if x0 == y0 == None or (x + x0) * 3 + (y + y0) + 1 in p:
                            p.append(num)
                            dfs(p)
                            p.pop()

        for num in range(1, 10):
            dfs([num])
        return self.ans


m = 4
n = 4
print Solution().numberOfPatterns(m, n)

