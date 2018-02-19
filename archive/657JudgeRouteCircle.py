# coding=utf-8
'''
Created on 2017å¹?8æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        p = [0, 0]
        for ch in moves:
            if ch == "U":
                p[0] += 1
            if ch == "D":
                p[0] -= 1
            if ch == "L":
                p[1] -= 1
            if ch == "R":
                p[1] += 1
        if p == [0, 0]:
            return True
        else:
            return False


moves = "LL"
print Solution().judgeCircle(moves)
