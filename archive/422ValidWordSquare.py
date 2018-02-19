# coding=utf-8
'''
Created on 2016å¹?12æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except Exception, e:
                    return False
        return True


words = [
  "ball",
  "area",
  "read",
  "lady"
]

print Solution().validWordSquare(words)
