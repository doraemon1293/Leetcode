# coding=utf-8
'''
Created on 2017å¹?5æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def foo(p1, p2, p3):
            arr = [distance(p1, p2), distance(p2, p3), distance(p3, p1)]
            if 0 in arr:
                return False
            if arr[0] == arr[1] and 2 * arr[0] == arr[2]:
                return True
            if arr[1] == arr[2] and 2 * arr[1] == arr[0]:
                return True
            if arr[2] == arr[0] and 2 * arr[2] == arr[1]:
                return True
            return False

        return foo(p1, p2, p3) and foo(p1, p2, p4) and foo(p1, p3, p4) and foo(p2, p3, p4)
