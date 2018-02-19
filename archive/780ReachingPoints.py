# coding=utf-8
'''
Created on 13 Feb 2018

@author: Administrator
'''


class Solution:

    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        if (sx, sy) == (tx, ty):
            return True
        while True:
            if tx > ty:
                if ty > sy:
                    tx %= ty
                elif ty < sy:
                    return False
                else:
                    return (tx - sx) % ty == 0
            elif tx < ty:
                if tx > sx:
                    ty %= tx
                elif tx < sx:
                    return False
                else:
                    return (ty - sy) % tx == 0
            else:
                return False

