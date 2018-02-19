# coding=utf-8
'''
Created on 2016å¹?11æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        letters = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        counters = [Counter(letter) for letter in letters]
        counter_s = Counter(s)
        ans = []
        seq = [(0, "z"), (6, "x"), (8, "g"), (7, "s"), (5, "v"), (4, "f"), (3, "r"), (2, "w"), (1, "o"), (9, "i")]
        for num, letter in seq:
            n = counter_s[letter]
            ans += str(num) * n
            for _ in xrange(n):
                counter_s.subtract(counters[num])
        return "".join(sorted(ans))


s = "fviefuro"
print Solution().originalDigits(s)

