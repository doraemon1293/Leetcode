class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        memo={}
        def foo(n,k):
            if (n,k) in memo: return memo[(n,k)]
            if k==1:
                memo[(n, k)] = sum(A[:n]) / n
                return memo[(n,k)]
            else:
                res=0
                temp_sum=0
                for i in range(n-1,0,-1):
                    temp_sum+=A[i]
                    res=max(res,foo(i,k-1)+temp_sum/(n-i))
                memo[(n,k)]=res
                return res
        N=len(A)
        return foo(N,K)



A = [9,1,2,3,9]
K = 3
print(Solution().largestSumOfAverages(A,K))
