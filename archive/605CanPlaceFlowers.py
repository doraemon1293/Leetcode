# coding=utf-8
'''
Created on 2017å¹?6æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flag = False
        left = 0
        while left < len(flowerbed) and flowerbed[left] == 0:
            left += 1
        if left == len(flowerbed):
            return (left + 1) / 2 >= n
        right = 0
        while flowerbed[-right - 1] == 0:
            right += 1
        n -= left / 2 + right / 2
        print left, right
        flag = False
        for x in flowerbed[left:-right if right != 0 else None]:
            if n <= 0: return True
            if flag:
                if x == 0:
                    count += 1
                else:
                    flag = False
                    n -= (count - 2 + 1) / 2
            else:
                if x == 0:
                    count = 1
                    flag = True
        return n <= 0


flowerbed = [0]

n = 1
print Solution().canPlaceFlowers(flowerbed, n)

