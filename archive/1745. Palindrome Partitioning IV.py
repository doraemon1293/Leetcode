import functools


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        @functools.lru_cache(None)
        def ispalindrome(st, end):
            if st == end:
                return True
            elif st > end:
                return True
            elif s[st] != s[end]:
                return False
            else:
                return ispalindrome(st + 1, end - 1)

        for i in range(len(s)):
            for j in range(i + 1, len(s) - 1):
                if ispalindrome(0, i) and ispalindrome(i + 1, j) and ispalindrome(j + 1, len(s) - 1):
                    print(i, j)
                    return True
        return False


print(Solution().checkPartitioning("bcbddxy"))
