class Solution:
    def makeGood(self, s: str) -> str:
        f = True
        while f and s:
            f = False
            for i in range(len(s) - 1):
                if s[i].islower() and s[i + 1] == s[i].upper() or s[i].isupper() and s[i + 1] == s[i].lower():
                    s = s[:i] + s[i + 2:]
                    f = True
                    break

        return s