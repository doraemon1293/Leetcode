class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        p1,p2=0,len(S)
        ans=[]
        for ch in S:
            if ch=="I":
                ans.append(p1)
                p1+=1
            else:
                ans.append(p2):
                p2-=1
        return ans
