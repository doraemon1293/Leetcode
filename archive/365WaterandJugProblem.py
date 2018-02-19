# coding=utf-8
'''
Created on 2017�?8�?18�?

@author: Administrator
'''


class Solution(object):

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # 倒一次等于水-x or -y 加一次等于水+x or +y
        # 题目转化�? 方程ax+by=z 有整数解(a,b)
        # 根据裴蜀定理（Bézout's lemma�?
        # ax+by=m有整数解时当且仅当m是d的�?�数�?(d为x y的最大公约数)
        if z > x + y:
            return False
        if z == 0:
            return True
        if x == 0 or y == 0:
            return z == max(x, y)
        while x % y:
            x, y = y, x % y
        return z % y == 0

