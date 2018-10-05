class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # ans=0
        # stack=[]
        # A=[float("inf")]+A+[float("inf")]
        # for i,a in enumerate(A):
        #     while stack and A[stack[-1]]>a:
        #         ind=stack.pop()
        #         ans+=A[ind]*(i-ind)*(ind-stack[-1])
        #     ans%=10**9+7
        # return ans

        stack=[]
        N=len(A)
        prev=[None]*N
        for i in range(N):
            while stack and A[i]<=stack[-1]:
                stack.pop()
            prev[i]=stack[-1] if stack else -1
        next_=[None]*N
        stack=[]
        for i in range(N,-1,-1):
            while stack and A[i]<stack[-1]:
                stack.pop()
            next_[i]=stack[-1] if stack else N
        return sum([A[i]*(i-prev[i])*(next_[i]-i) for i in range(N)])


