class Solution:
    def minimumTime(self, s: str) -> int:
        ans = 0
        dp_1 = 0
        for ch in s:
            if ch == "1":
                dp = min(dp_1 + 1, 1)
            if ch == "0":
                dp = min(dp_1 - 1, -1)
            ans = min(ans, dp)
            dp_1=dp
        return len(s)+ans
