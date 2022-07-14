class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans=[]
        for a in range(ord(s[3])-ord(s[0])+1):
            for b in range(int(s[1]),int(s[-1])+1):
                ans.append(chr(ord(s[0])+a)+str(b))
        return ans
s = "A1:F1"
print(Solution().cellsInRange(s))