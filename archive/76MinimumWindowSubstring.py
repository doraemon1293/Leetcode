# coding=utf-8
'''
Created on 2017å¹?5æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == "" or t == "": return ""
        from collections import Counter
        count = Counter(t)
        for k in count:
            count[k] *= -1
        st = en = 0
        mini = 2 ** 31 - 1
        ans = ""
        flag = False
        for en in range(len(s)):
            if s[en] in count:
                count[s[en]] += 1
            if count[s[en]] == 0:
                flag = all(map(lambda x:x >= 0, count.values()))
            while flag:
                if mini > en - st + 1:
                    mini = en - st + 1
                    ans = (st, en)
                if s[st] in count:
                    count[s[st]] -= 1
                    if count[s[st]] < 0:
                        flag = False
                st += 1
        # print ans
        return s[ans[0]:ans[1] + 1]  if ans != "" else ans


s = "ab"
t = "b"
print repr(Solution().minWindow(s, t))
