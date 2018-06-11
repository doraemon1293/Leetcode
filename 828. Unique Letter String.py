class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        import bisect
        s=set(S)
        d={}
        for i,ch in enumerate(S):
            d.setdefault(ch,[])
            d[ch].append(i)
        ans=0
        for i in range(len(S)):
            for ch in s:
                l=d[ch]
                ind=bisect.bisect_left(l,i)
                if ind<len(l)-1:
                    ans+=l[ind+1]-l[ind]
                elif ind==len(l)-1:
                    ans+=len(S)-l[ind]
                ans%=10**9+7
        return ans
S="ABA"
S="ABC"
print(Solution().uniqueLetterString(S))




