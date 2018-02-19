# coding=utf-8
'''
Created on 2017å¹?4æœ?11æ—?

@author: Administrator
'''
from collections import Counter


class Solution(object):

    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """

        possible_row = set()
        possible_col = set()
        d = {}
        for i in xrange(len(picture)):
            summ = len([j for j in xrange(len(picture[i])) if picture[i][j] == "B"])
            if summ == N:
                possible_row.add(i)
        for j in xrange(len(picture[0])):
            summ = len([i for i in xrange(len(picture)) if picture[i][j] == "B"])
            if summ == N:
                possible_col.add(j)
        for i in xrange(len(picture)):
            s = "".join(picture[i])
            d.setdefault(s, set())
            d[s].add(i)
        ans = 0
        for row in possible_row:
            for col in possible_col:
                if picture[row][col] == "B":
                    flag = True
                    s = "".join(picture[row])
                    # print row, col
                    # print [x for x in xrange(len(picture)) if picture[x][col] == "B"]
                    for i in [x for x in xrange(len(picture)) if picture[x][col] == "B"]:
                        if i not in d[s]:
                            flag = False
                            break
                    if flag:
                        print col, row
                        ans += 1
        return ans


picture = ["WBBWWBWWWWWBBWW",
         "WBBWWBWWWWWBBWW",
         "WWWWWBBBWBWWWWB",
         "WWBWBWWWWBBWBWW",
         "WBBWWBWWWWWBBWW",
         "WWBWBWWWWBBWBWW",
         "WWBWBWWWWBBWBWW",
         "WWBWBWWWWBBWBWW"]
N = 5
print Solution().findBlackPixel(picture, N)

