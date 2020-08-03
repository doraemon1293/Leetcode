class Solution:
    def countLetters(self, S: str) -> int:
        s = S[0]
        ans = 1

        for ch in S[1:]:
            if ch == s[0]:
                s += ch
                ans += len(s)
            else:
                s = ch
                ans += len(s)
        return ans
