class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        maxi = [None] * N
        maxi[0] = A[0]
        mini = [None] * N
        mini[-1] = A[-1]
        for i in range(1, N):
            maxi[i] = max(A[i], maxi[i - 1])
        for i in range(N - 2, -1, -1):
            mini[i] = min(A[i], mini[i + 1])
        for i in range(N - 1):
            if maxi[i] <= mini[i + 1]:
                return i + 1
