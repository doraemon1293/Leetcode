class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        from collections import  Counter
        counter=Counter(T)
        ans=[]
        for ch in S:
            if ch in counter:
                ans.extend([ch]*counter[ch])
                del counter[ch]
        for ch in counter:
            ans.extend([ch]*counter[ch])
        return "".join(ans)
S="cba"
T="abcd"
print(Solution().customSortString(S,T))