# coding=utf-8
'''
Created on 2017å¹?7æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r = 0
        senate = list(senate)
        print senate
        while "R" in senate and "D" in senate:
            for i in xrange(len(senate)):
                if senate[i] != "0":
                    if r == 0:
                        if senate[i] == "R":
                            r += 1
                        else:
                            r -= 1
                    elif r > 0:
                        if senate[i] == "R":
                            r += 1
                        else:
                            senate[i] = "0"
                            r -= 1
                    else:
                        if senate[i] == "D":
                            r -= 1
                        else:
                            senate[i] = "0"
                            r += 1
            senate = [x for x in senate if x != "0"]
            # print senate, r
        if "R" in senate:
            return "Radiant"
        else:
            return "Dire"


senate = "RDD"
print Solution().predictPartyVictory(senate)

