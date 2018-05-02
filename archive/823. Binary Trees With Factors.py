class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        memo = {}
        for a in A:
            memo[a]=1
        ans = 0
        for i in range(len(A)):
            a = A[i]
            j=0
            while A[j]*A[j]<=a:
                b = A[j]
                if a % b==0 and a // b in memo:
                    c = a / b
                    memo[a] += (2 if b != c else 1) * memo[b] * memo[c] % (10 ** 9 + 7)
                j+=1
            ans += memo[a]
            ans%=10**9+7
        return ans



A = [2, 4, 16]
A = [2, 4, 5, 10]
#A=[2,3,6]
print(Solution().numFactoredBinaryTrees(A))
