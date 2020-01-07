class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        d = {}

        for i in range(len(S)):
            for j in range(i + 1, len(S) + 1):
                s = S[i:j]
                d.setdefault(s, 0)
                d[s] += 1
        return max([len(s) for s in d if d[s] > 1] or [0])
