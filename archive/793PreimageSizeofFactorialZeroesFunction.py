# coding=utf-8
class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def trailingZero(n):
            res=0
            while n:
                res+=n//5
                n//=5
            return res

        n=4*K
        t=0
        while t<=K:
            t=trailingZero(n)
            #print(n,t)
            n+=1
            if t==K:
                return 5
        return 0
print(Solution().preimageSizeFZF(5))