class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i=0
        st=0
        ans=[]
        while i<=len(S):
            if i==len(S) or S[i]!=S[i-1]:
                if i-st>=3:
                    ans.append([st,i-1])
                st=i
            else:
                pass
            i+=1
        return ans

S="abbxxxxzzz"
S="abcdddeeeeaabbb"
print(Solution().largeGroupPositions(S))


