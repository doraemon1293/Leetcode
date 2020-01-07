class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        ans = -float("inf")
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] < K:
                    ans = max(ans, A[i] + A[j])
        return ans if ans!=-float("inf") else -1
