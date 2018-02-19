# coding=utf-8
'''
Created on 2016å¹?12æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strings:
            k = tuple((ord(s[i]) - ord(s[i + 1])) % 26 for i in xrange(0, len(s) - 1))
            groups.setdefault(k, [])
            groups[k].append(s)
            print k, s
        return groups.values()


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print Solution().groupStrings(strings)
