# coding=utf-8
'''
Created on 9 Jan 2018

@author: Administrator
'''
from itertools import product


class Solution:

    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from itertools import product
        from collections import defaultdict
        d = defaultdict(list)
        for a, b, c in allowed:
            d[a, b].append(c)

        def dfs(bottom):
            if len(bottom) == 1:
                return True
            options = []
            for i in range(len(bottom) - 1):
                options.append(d[bottom[i], bottom[i + 1]])
            for row in product(*options):
                if dfs(row):
                    return True
            return False

        return dfs(bottom)
