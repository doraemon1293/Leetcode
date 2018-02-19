# coding=utf-8
'''
Created on 2017å¹?4æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if picture:
            rows = [0] * len(picture)
            cols = [0] * len(picture[0])
            for row in range(len(picture)):
                for col in range(len(picture[row])):
                    if picture[row][col] == "B":
                        rows[row] += 1
                        cols[col] += 1
            ans = 0
            for row in range(len(picture)):
                for col in range(len(picture[row])):
                    if rows[row] == 1 and cols[col] == 1 and picture[row][col] == "B":
                        ans += 1

            return ans
        else:
            return 0


picture = ["BBB"]
print Solution().findLonelyPixel(picture)
