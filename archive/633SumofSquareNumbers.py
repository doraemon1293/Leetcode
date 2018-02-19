class Solution(object):

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        n = int(c ** 0.5)
        for a in xrange(n + 1):
            b = int((c - a ** 2) ** 0.5)
            if b ** 2 + a ** 2 == c:
                return True
        return False


c = 0
print Solution().judgeSquareSum(c)
