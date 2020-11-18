class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        memo={}
        MOD=10**9+7
        def foo(n,k):
            if (n,k) in memo:
                return memo[n,k]
            if n-1==k:
                res=1
            elif n-1<k:
                res=0
            elif k==0:
                res=1
            elif k==1:
                res= n*(n-1)//2
            else:
                res=0
                for n_mid in range(1,n-1):
                    n_left=n_mid+1
                    n_right=n-n_mid
                    for k_left in range(0,k+1):
                        k_right=k-k_left
                        res+=foo(n_left,k_left)*foo(n_right,k_right)
                res%=MOD
            memo[n,k]=res
            return res
        foo(n,k)
        print(memo[n,k])


# print(Solution().numberOfSets(n = 3, k = 1))
print(Solution().numberOfSets(n = 633, k = 64))



