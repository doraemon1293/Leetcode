import collections


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        c = collections.Counter(A)
        return max([k for k in c if c[k] == 1] + [-1])
