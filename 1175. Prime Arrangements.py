class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        self.primes = []

        def is_prime(n):
            if n == 2:
                self.primes.append(n)
                return True
            for i in self.primes:
                if n % i == 0:
                    return False
            self.primes.append(n)
            return True

        for i in range(2, n + 1):
            is_prime(i)

        def fac(n):
            res = 1
            for i in range(1, n + 1):
                res *= i
            return res

        return fac(len(self.primes))*fac(n-len(self.primes))%(10**9+7)
print(Solution().numPrimeArrangements(5))