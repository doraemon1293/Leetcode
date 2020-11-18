class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(len(t)):
                mismatch = 0
                i1, j1 = i, j
                # print(ii,jj)
                while mismatch<2 and i1 < len(s) and j1 < len(t):
                    if s[i1] != t[j1]:
                        mismatch += 1
                    if mismatch == 1:
                        ans += 1
                    i1 += 1
                    j1 += 1

        return ans


s = "aba"
t = "baba"
s = "abe"
t = "bbc"
print(Solution().countSubstrings(s, t))
