class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        N=len(S)
        S=list(s)
        i,j=0,N-1
        while i<j:
            while i<j and not S[i].isalpha():
                i+=1
            while i<j and not S[j].isalpha():
                j-=1
            if i<j:
                S[i],S[j]=S[j],S[i]
        return "".join(S)