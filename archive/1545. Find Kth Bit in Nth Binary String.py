class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length=[1]
        for i in range(1,n+1):
            length.append(length[-1]*2+1)

        def solve(n,k):
            if n==0:
                return 0
            if k==length[n]//2+1:
                return 1
            elif k<=length[n]//2:
                return solve(n-1,k)
            else:
                return solve(n-1,length[n-1]-(k-length[n]//2-1)+1)^1
        return str(solve(n,k))