class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        not_found = {}

        def find(target, k, i):
            if not_found.get((target, k), N+1) <= i:
                return False
            if k == 0:
                return target == 0
            if k > N - i:
                return False
            res = (find(target - A[i], k - 1, i + 1) if A[i]<=target else False) or find(target, k, i + 1)
            if not res:
                not_found[(target, k)] = min(not_found.get((target, k), N+1), i)
            return res

        ave = sum(A) / N
        for lenB in range(1, N // 2 + 1):
            target = ave * lenB
            if abs(target - int(target)) < 10 ** (-6):
                target = int(target)
                if find(target, lenB, 0):

                    return True
        return False


A = [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]
A=[3,1,2]
print(Solution().splitArraySameAverage(A))
