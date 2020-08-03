class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        st = 0
        ans = 1
        while st < len(A) - 1:
            end = st
            if A[end] != A[end + 1]:
                flag = A[end] < A[end + 1]
                while end < len(A) - 1 and A[end] != A[end + 1] and (A[end] < A[end + 1]) == flag:
                    end += 1
                    flag = not flag
                ans = max(ans, end - st + 1)
                st = end
            else:
                st = end + 1
        return ans


A = [9, 4, 2, 10, 7, 8, 8, 1, 9]
# A=[100,100]
A = [4, 8, 12, 16]

print(Solution().maxTurbulenceSize(A))
