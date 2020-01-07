class Solution:
    def longestOnes(self, A, K):
        left = right = 0
        ans = 0
        while left < len(A):
            while right < len(A) and (K or A[right]==1) :
                if A[right] == 1:
                    right += 1
                    ans = max(ans, right - left)
                else:
                    K -= 1
                    right+=1
                    ans = max(ans, right - left)
            while left < len(A) and A[left] == 1:
                left += 1
            K += 1
            left+=1
            print(left,right)
        return ans


A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 3
print(Solution().longestOnes(A, K))
