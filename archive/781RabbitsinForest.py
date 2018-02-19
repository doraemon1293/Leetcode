# coding=utf-8
'''
Created on 12 Feb 2018

@author: Administrator
'''


class Solution(object):

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        from math import ceil
        count = Counter(answers)
        ans = 0
        print(count)
        for k, v in count.items():
            print((k + 1) * int(ceil(v / (k + 1))), k, v)
            ans += (k + 1) * int(ceil(v / (k + 1)))
        return ans


answers = [0, 0, 1, 1, 1]
print(Solution().numRabbits(answers))
