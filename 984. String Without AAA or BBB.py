class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A>=B:
            a="a"
            b="b"
        else:
            a="b"
            b="a"
            A,B=B,A
        ans=""
        temp=min(A-B,B,A//2)
        ans+=(a+a+b)*temp
        A-=temp*2
        B-=temp
        if A==B:
            ans+=(a+b)*A
        if A==0:
            ans+=b*B
        if B==0:
            ans+=a*A
        return ans
