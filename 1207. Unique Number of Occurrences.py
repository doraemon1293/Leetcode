import collections


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = collections.Counter(arr)
        return len(c.values()) == len(set(c.values()))

