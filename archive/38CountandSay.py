# coding=utf-8
'''
Created on 2016å¹?11æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        for x in range(1, n + 1):
            if x == 1:
                ans = "1"
            else:
                next = ""
                current_c = ans[0]
                current_count = 1
                for c in ans[1:]:
                    if c == current_c:
                        current_count += 1
                    else:
                        next += str(current_count) + current_c
                        current_c = c
                        current_count = 1
                next += str(current_count) + current_c
                ans = next
        return ans


print Solution().countAndSay(5)

