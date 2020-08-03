class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(a,b):
            a,b=max(a,b),min(a,b)
            while a%b:
                a,b=b,a%b
            return b



        low = 1
        high = 2 * (10 ** 9)
        ab = a * b // gcd(a, b)
        bc = b * c // gcd(b, c)
        ac = a * c // gcd(a, c)
        abc = ab * c // (gcd(ab, c))

        def foo(n):
            return n // a + n // b + n // c - n // ab - n // ac - n // bc + n // abc

        while low <= high:
            mid = (low + high) // 2
            temp = foo(mid)
            print(mid, temp, low, high)
            if temp == n:
                if mid % a == 0 or mid % b == 0 or mid % c == 0:
                    return mid
                else:
                    high = mid - 1
            elif temp < n:
                low = mid + 1
            else:
                high = mid - 1
