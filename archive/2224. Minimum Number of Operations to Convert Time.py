class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        ans=0
        h1,m1=[int(x) for x in current.split(":")]
        h2,m2=[int(x) for x in correct.split(":")]
        mins=(h2-h1)*60+(m2-m1)
        for x in (60,15,5,1):
            ans+=mins//x
            mins=mins%x
        return ans
