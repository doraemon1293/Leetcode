class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        p1, p2 = 0, 1
        N = len(A)
        while p1 < N and p2 < N:
            while p1 < N and A[p1] % 2 == 0:
                p1 += 2
            while p2 < N and A[p2] % 2:
                p2 += 2
            if p1 < N and p2 < N: A[p1], A[p2] = A[p2], A[p1]
        return A
A=[2,0,3,4,1,3]
print(Solution().sortArrayByParityII(A))