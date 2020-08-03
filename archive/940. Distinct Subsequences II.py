from collections import defaultdict


class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        last = defaultdict(int)
        dp = [1]
        MOD = 10 ** 9 + 7
        for i, ch in enumerate(S):
            temp = (dp[-1] * 2 - last[ch]) % MOD
            dp.append(temp)
            last[ch] = dp[-2]
            print(dp, last)
        return (dp[-1] - 1) % MOD


print(Solution().distinctSubseqII("abab"))
