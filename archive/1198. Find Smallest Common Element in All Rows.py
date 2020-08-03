import collections


class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        c = collections.Counter()
        low = max([row[0] for row in mat])
        high = min([row[-1] for row in mat])
        for row in mat:
            for a in row:
                c[a] += 1

        for a in range(low, high):
            if c[a] == len(mat):
                return a
