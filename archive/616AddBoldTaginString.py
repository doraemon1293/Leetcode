# coding=utf-8
'''
Created on 2017å¹?6æœ?11æ—?

@author: Administrator
'''

import re


class Solution(object):

    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        intervals = []
        for sub_s in dict:
            intervals.extend([[m.start(), m.start() + len(sub_s) - 1] for m in re.finditer('(?=%s)' % sub_s, s)])
        intervals.sort(key = lambda x: x[0])
        print intervals
        if intervals == []: return s
        new_interval = [intervals[0]]
        for interval in intervals[1:]:
            if new_interval[-1][1] + 1 >= interval[0]:
                new_interval[-1][1] = max(interval[1], new_interval[-1][1])
            else:
                new_interval.append(interval)
        print new_interval
        intervals = new_interval
        print intervals
        ans = ""
        st = 0
        for interval in intervals:
            ans += s[st:interval[0]]
            ans += "<b>" + s[interval[0]:interval[1] + 1] + "</b>"
            st = interval[1] + 1
        ans += s[st:]
        return ans


s = "aaabbcc"
dict = ["aaa", "aab", "bc"]
s = "abcxyz123"
dict = ["abc", "123"]
s = "aaabbcc"
dict = ["aaa", "aab", "bc", "aaabbcc"]

print Solution().addBoldTag(s, dict)
