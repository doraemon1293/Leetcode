import collections
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c=collections.Counter(s)
        return len(set(c.values()))==1
