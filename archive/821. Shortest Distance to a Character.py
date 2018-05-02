class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        inds=[-float("inf")]+[i for i, c in enumerate(S) if c==C]+[float("inf")]
        ans=[]
        p=0
        for i in range(len(S)):
            ans.append(min(abs(i-inds[p]),abs(i-inds[p+1])))
            if i==inds[p+1]:
                p+=1
        return ans
S = "loveleetcode"
C = 'e'
print(Solution().shortestToChar(S,C))


