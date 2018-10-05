class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        import collections
        counter=collections.Counter(str(N))
        t=1
        temp_counter=collections.Counter(str(t))
        if temp_counter==counter:
            return True
        while t<=10**9:
            t*=2
            temp_counter=collections.Counter(str(t))
            if temp_counter==counter:
                return True
        return False





N=254432353
print(Solution().reorderedPowerOf2(N))
