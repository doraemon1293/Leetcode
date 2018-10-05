class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        def gcd(A,B):
            while A%B:
                A,B=B,A%B
            return B
        LCM=A*B//gcd(A,B)
        print(LCM)
        def magic(x):
            return x//A+x//B-x//LCM

        lo=0
        hi=N*A
        while lo<hi:
            mid=(hi+lo)//2
            if magic(mid)<N:
                lo=mid+1
            else:
                hi=mid
        return lo%(10**9+7)
