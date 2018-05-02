class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        memo={}
        def foo(a,b,recursion):
            if recursion>100:
                return 1
            if (a,b) in memo: return memo[(a,b)]
            if a<=0 and b<=0:
                return 0.5
            if a<=0:
                return 1
            if b<=0:
                return 0
            memo[(a,b)]=0.25*((foo(a-100,b,recursion+1))+foo(a-75,b-25,recursion+1)+foo(a-50,b-50,recursion+1)+foo(a-25,b-75,recursion+1))
            return memo[(a,b)]
        return foo(N,N,0)
N=800
print(Solution().soupServings(N))