# coding=utf-8
'''
Created on 9 Jan 2018

@author: Administrator
'''


class Solution:

    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = "0"*(n - 1)
        visited = set()
        for _ in range(k ** n):
            prefix = ans[-(n - 1):] if n - 1 > 0 else ""
            for x in range(k - 1, -1, -1):
                if prefix + str(x) not in visited:
                    visited.add(prefix + str(x))
                    ans += str(x)
                    break
        return ans


n = 2
k = 2
print(Solution().crackSafe(n, k))
