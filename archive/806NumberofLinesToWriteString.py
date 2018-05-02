class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        alphaWid={}
        lines=1
        cur=0
        for i in range(len(widths)):
            alphaWid[chr(ord("a")+i)]=widths[i]
        for ch in S:
            w=widths[ord(ch)-ord("a")]
            if cur+w<=100:
                cur+=w
            else:
                lines+=1
                cur=w
        if cur==0: lines-=1
        return lines,cur

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
print(Solution().numberOfLines(widths,S))


