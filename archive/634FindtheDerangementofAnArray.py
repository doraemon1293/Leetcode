class Solution(object):

    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        d1 = 0
        d2 = 1
        for i in xrange(3, n + 1):
            d3 = ((i - 1) * (d1 + d2)) % (10 ** 9 + 7)
            d1 = d2 % (10 ** 9 + 7)
            d2 = d3 % (10 ** 9 + 7)
        return d3


n = 3
print Solution().findDerangement(n)
