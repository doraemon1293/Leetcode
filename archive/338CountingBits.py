# coding=utf-8
'''
Created on 2016å¹?11æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        ans = [1]
        temp = [1]
        while len(ans) < num:
            temp.extend([x + 1 for x in temp])
            ans.extend(temp)
        ans.insert(0, 0)
        return ans[:num + 1]


print Solution().countBits(1)

