class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        for i, ch in enumerate(s):
            d.setdefault(ch, [float("inf"), -float("inf")])
            d[ch][0] = min(d[ch][0], i)
            d[ch][1] = max(d[ch][1], i)
        return max([d[ch][1] - d[ch][0] - 1 for ch in d] + [-1])
