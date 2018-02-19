# coding=utf-8
'''
Created on 2017å¹?11æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        self.memo = {}

        def preProcess(S):
            nextInd = {}
            forwardInd = {}
            cur = {}
            for i in xrange(len(S) - 1, -1, -1):
                cur[S[i]] = i
                for ch in ("a", "b", "c", "d"):
                    nextInd[i, ch] = cur.get(ch, None)
            cur = {}
            for i in xrange(len(S)):
                cur[S[i]] = i
                for ch in ("a", "b", "c", "d"):
                    forwardInd[i, ch] = cur.get(ch, None)
            return nextInd, forwardInd

        nextInd, forwardInd = preProcess(S)
#         print nextInd
#         print forwardInd
        MOD = 10 ** 9 + 7

        def dp(st, end):
            if st > end:
                return 0
            if (st, end) in self.memo:
                return self.memo[st, end]
            else:
                res = 0
                for ch in ("a", "b", "c", "d"):
                    st0 = nextInd[st, ch]
                    end0 = forwardInd[end, ch]
                    if st0 != None:
                        if st0 < end0:
                            res += 1
                        if st0 <= end:
                            res += dp(st0 + 1, end0 - 1) + 1
                res %= MOD
                self.memo[st, end] = res
                return res

        return dp(0, len(S) - 1)


S = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
# S = "bccb"
# S = "a"
print Solution().countPalindromicSubsequences(S)

