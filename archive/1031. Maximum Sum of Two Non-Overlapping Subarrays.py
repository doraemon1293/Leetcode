class Solution:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
        sum_L=[sum(A[0:L])]
        for i in range(1,len(A)-L+1):
            temp=sum_L[-1]
            temp=temp-A[i-1]+A[i+L-1]
            sum_L.append(temp)
        sum_M=[sum(A[0:M])]
        for i in range(1,len(A)-M+1):
            temp=sum_M[-1]
            temp=temp-A[i-1]+A[i+M-1]
            sum_M.append(temp)

        ans=-float("inf")
        for i in range(sum_L):
            for j in range(i+L,len(A)-M+1):
                ans=max(ans,sum_L[i]+sum_M[j])

        for i in range(sum_M):
            for j in range(i+M,len(A)-L+1):
                ans=max(ans,sum_M[i]+sum_L[j])

        return ans

A=[0,6,5,2,2,5,1,9,4]
L=1
M=2
print(Solution().maxSumTwoNoOverlap(A,L,M))