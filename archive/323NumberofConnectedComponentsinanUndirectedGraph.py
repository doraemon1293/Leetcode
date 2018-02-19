# coding=utf-8
'''
Created on 2017å¹?5æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        def dfs(n):
            s.discard(n)
            for x in n_nodes[n]:
                if x in s:
                    dfs(x)

        s = set(range(n))
        n_nodes = [set() for i in range(n)]
        for x, y in edges:
            n_nodes[x].add(y)
            n_nodes[y].add(x)
        ans = 0
        for i in range(n):
            if s == set():
                break
            if i in s:
                ans += 1
                dfs(i)
        return ans


print Solution().countComponents(5,
[[0, 1], [1, 2], [3, 4]])

