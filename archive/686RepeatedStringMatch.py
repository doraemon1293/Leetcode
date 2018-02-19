# coding=utf-8
'''
Created on 2017å¹?10æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import math
        rotations = {}
        for head in xrange(len(A)):
            rotations.setdefault(A[head:] + A[:head], head)
        if B == "": return 0
        if A == "": return -1
        if len(B) < len(A):
            if B in A:
                return 1
            else:
                for s in rotations:
                    if B in s:
                        return 2
            return -1
        else:
            for i in xrange(len(B) - len(A) + 1):
                if B[i:i + len(A)] not in rotations:
                    return -1
            head = rotations[B[:len(A)]]
            return int(math.ceil(float(len(B)) / len(A))) + (1 if head != 0 else 0)


A = "a"
B = "aa"
A = "bb"
B = "bbbbbbb"
print Solution().repeatedStringMatch(A, B)
