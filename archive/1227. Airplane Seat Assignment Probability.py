class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        dp = 1
        for i in range(2, n+1):
            new_dp = 1 / i + dp * (i - 2) / i
            dp = new_dp
        return dp


