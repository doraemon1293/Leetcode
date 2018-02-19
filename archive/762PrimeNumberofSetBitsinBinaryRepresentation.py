class Solution:

    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        ans = 0
        for n in range(L, R + 1):
            if bin(n)[2:].count("1") in primes:
                ans += 1
        return ans


L = 6
R = 10
print(Solution().countPrimeSetBits(L, R))
