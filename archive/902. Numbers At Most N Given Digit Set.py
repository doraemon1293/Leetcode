class Solution:
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        len_N=len(str(N))
        ans=sum([len(D)**i for i in range(1,len_N)])
        def f(D,n):
            if n:
                a=n[0]
                temp=0
                for d in D:
                    if d<a:
                        temp+=1
                res=temp*(len(D)**(len(n)-1))
                if a in D:
                    res+=f(D,n[1:])
                return res
            else:
                return 1
        ans+=f(D,str(N))
        return ans
D=["3","4","8"]
N=4
print(Solution().atMostNGivenDigitSet(D,N))