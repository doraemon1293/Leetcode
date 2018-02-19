# coding=utf-8
'''
Created on 2017å¹?7æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
# Let's keep track of:
#
# e0 = current number of ways we could decode, ending on any number;
# e1 = current number of ways we could decode, ending on an open 1;
# e2 = current number of ways we could decode, ending on an open 2;
# (Here, a "open 1" means a 1 that may later be used as the first digit of a 2 digit number, because it has not been used in a previous 2 digit number.)
#
# With the right idea of what to keep track of, our dp proceeds straightforwardly.
#
# Say we see some character c. We want to calculate f0, f1, f2, the corresponding versions of e0, e1, e2 after parsing character c.
#
# If c == '*', then the number of ways to finish in total is: we could put * as a single digit number (9*e0), or we could pair * as a 2 digit number 1* in 9*e1 ways, or we could pair * as a 2 digit number 2* in 6*e2 ways. The number of ways to finish with an open 1 (or 2) is just e0.
#
# If c != '*', then the number of ways to finish in total is: we could put c as a single digit if it is not zero ((c>'0')*e0), or we could pair c with our open 1, or we could pair c with our open 2 if it is 6 or less ((c<='6')*e2). The number of ways to finish with an open 1 (or 2) is e0 iff c == '1' (or c == '2').
#
#

        MOD = 10 ** 9 + 7
        f0, f1, f2 = 1, 0, 0
        for ch in s:
            if ch == "*":
                new_f0 = 9 * f0 + 9 * f1 + 6 * f2
                new_f1 = f0
                new_f2 = f0
            else:
                new_f0 = (f0 if ch != "0" else 0) + f1 + (f2 if ch <= "6" else 0)
                new_f1 = f0 if ch == "1" else 0
                new_f2 = f0 if ch == "2" else 0
            f0, f1, f2 = new_f0 % MOD , new_f1, new_f2
        return f0


s = "1*"
print Solution().numDecodings(s)
