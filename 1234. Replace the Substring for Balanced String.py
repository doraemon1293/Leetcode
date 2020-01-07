import collections


class Solution:
    def balancedString(self, s: str) -> int:
        right = 0
        n = len(s)
        counter = collections.Counter(s)
        c = collections.defaultdict(int)

        def foo():
            for ch in ("Q", "W", "E", "R"):
                if c[ch] < counter[ch] - n // 4:
                    return False
            return True

        ans = 0
        for left in range(n):
            if left != 0:
                c[s[left - 1]] -= 1

            while right < len(s) and foo() == False:
                c[s[right]] += 1
                right += 1
            if foo():
                ans = min(ans, right - left)
        return ans