class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        def isprime(n):
            return n > 1 and all(n % x for x in range(2, int(n ** 0.5) + 1))

        if N <= 11:
            while not isprime(N) or str(N) != str(N)[::-1]:
                N += 1
            return N
        else:
            s = str(N)
            length = len(s)
            if length % 2 == 0:
                root = int("1" + "0" * (length // 2))
            else:
                root = int(s[:length // 2 + 1])
            n = int(str(root) + str(root)[:-1][::-1])
            while n < N:
                root += 1
                n = int(str(root) + str(root)[:-1][::-1])
            while not isprime(n):
                root += 1
                n = int(str(root) + str(root)[:-1][::-1])
            return n


N = 6000
print(Solution().primePalindrome(N))
