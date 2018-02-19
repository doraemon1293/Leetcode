# coding=utf-8
'''
Created on 2016å¹?11æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        from itertools import combinations

        ans = []
        for comb in combinations(range(10), num):
            h = m = 0
            for x in comb:
                if x < 4:
                    h += 2 ** x
                else:
                    m += 2 ** (x - 4)
            if h < 12 and m < 60:
                ans.append(str(h) + ":" + str(m).zfill(2))
        return sorted(ans)


print Solution().readBinaryWatch(2)

