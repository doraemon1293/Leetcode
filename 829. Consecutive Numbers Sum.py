class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        #2N=k(2x+k+1)
        ans=0
        for k in range(1,int(((2*N)**0.5))+1):
            if 2*N%k==0:
                x=2*N//k-k-1
                if x%2==0:
                    ans+=1

        return ans

N=822098
N=15
print(Solution().consecutiveNumbersSum(N))


