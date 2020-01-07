from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c_b = Counter("balloon")
        c = Counter(text)
        ans = float("inf")
        for k in c_b:
            ans = min(ans, c[k] // c_b[k])
        return ans
