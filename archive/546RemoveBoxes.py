# coding=utf-8
'''
Created on 2017å¹?10æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        if boxes == []: return 0
        length = []
        c = []
        cur_c = boxes[0]
        l = 1
        for box in boxes[1:] + [None]:
            if box != cur_c:
                length.append(l)
                c.append(cur_c)
                cur_c = box
                l = 1
            else:
                l += 1
        memo = {}

        def foo(i, j, k):
            if i > j:
                return 0
            if (i, j, k) in memo:
                return memo[i, j, k]
            res = foo(i, j - 1, 0) + (length[j] + k) ** 2
            for x in range(i, j):
                if c[x] == c[j]:
                    res = max(res, foo(i, x, length[j] + k) + foo(x + 1, j - 1, 0))
            memo[i, j, k] = res
            return res

        return foo(0, len(length) - 1, 0)


boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
print Solution().removeBoxes(boxes)
