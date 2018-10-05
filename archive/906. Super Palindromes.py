class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        n=1
        ans=0
        while True:
            s=str(n)
            s1=int(s+s[::-1])**2
            s2=int(s+s[:-1][::-1])**2
            ans+=str(s1)==str(s1[::-1]) and L<=s1<=R
            ans+=str(s2)==str(s2[::-1]) and L<=s2<=R
            if int(s1)>R and int(s2)>R:
                return ans