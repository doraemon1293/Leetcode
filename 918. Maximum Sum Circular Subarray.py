class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        temp_min_sum = A[0]
        min_sum = A[0]
        temp_max_sum = A[0]
        max_sum = A[0]
        for a in A[1:]:
            temp_min_sum = min(a, temp_min_sum + a)
            min_sum = min(min_sum, temp_min_sum)
            temp_max_sum = max(a, temp_max_sum + a)
            max_sum = max(max_sum, temp_max_sum)
        if max_sum > 0:
            ans = max(max_sum, sum(A) - min_sum)
        else:
            ans = max_sum
        return ans


A = [-5, -3, -5]
# A = [1,-2,3,-2]

print(Solution().maxSubarraySumCircular(A))
