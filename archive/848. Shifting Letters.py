class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        S=list(S)
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        for i in range(len(shifts)):
            S[i]=chr(ord("a")+(ord(S[i])-ord("a")+shifts[i])%26)
        return "".join(S)