# coding=utf-8
'''
Created on 2017å¹?10æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        count = Counter(s)
        ch_set = set()
        ans = []
        for ch in s:
            count[ch] -= 1
            if ch not in ch_set:
                while ans and ans[-1] > ch and count[ans[-1]] > 0:
                    ch_set.remove(ans[-1])
                    ans.pop()
                ans.append(ch)
                ch_set.add(ch)
        return "".join(ans)


s = "bcabc"
s = "cbacdcbc"
s = "aaaa"
s = "abacb"
print Solution().removeDuplicateLetters(s)

