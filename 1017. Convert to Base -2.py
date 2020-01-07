class Solution:
    def baseNeg2(self, N: int) -> str:
        res=[]
        while N:
            if N%(-2)==0:
                res.append(0)
                N/=(-2)
            if N%(-2)==-1:
                N=(N-1)/(-2)
                res.append(1)
        return "".join([str(x) for x in res[::-1]])



