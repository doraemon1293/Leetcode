class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        memo={}
        def f(k,n):
            if n==0:
                return 0
            if k==1:
                return n
            if (k,n) in memo:
                return memo[k,n]
            lo,hi=1,n
            while lo+1<hi:
                x=(lo+hi)//2
                t1=f(k-1,x-1)
                t2=f(k,n-x)
                if t1<t2:
                    lo=x
                elif t1>t2:
                    hi=x
                else:
                    lo=hi=x
            res = 1 + min([max(f(k - 1, x - 1), f(k, n - x)) for x in (lo, hi)])
            memo[k,n]=res
            return res

        return f(K,N)


print(Solution().superEggDrop(2,6))