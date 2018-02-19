# coding=utf-8
'''
Created on 2017�?11�?23�?

@author: Administrator
'''


# Manacher's ALGORITHM: O(n)时间求字符串的最长回文子�?
# https://www.felix021.com/blog/read.php?2040
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = ["$", "#"]
        for ch in s:
            chars.append(ch)
            chars.append("#")
        chars.append("|")
        s = "".join(chars)
        p = [0] * len(s)
        mx = id = 0
        longest = -1
        longestCenter = -1
        for i in xrange(1, len(s) - 1):
            p[i] = min(p[2 * id - i], mx - i) if mx > i else 1
            while s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
            if p[i] + i > mx:
                mx = i + p[i]
                id = i
            if p[i] > longest:
                longest = p[i]
                longestCenter = i
        return filter(lambda ch:ch != '#', s[longestCenter - longest + 1:longestCenter + longest])


s = "aaabaaaa"

print Solution().longestPalindrome(s)

