from collections import deque


class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        if K == 1:
            return A.count(0)
        ans = 0
        flips = 0
        end_points = deque()
        p = 0

        while p < len(A):
            # find leftmost 0
            while p < len(A):
                while end_points and end_points[0] <= p:
                    end_points.popleft()
                    flips^=1
                A[p] = A[p] ^ flips
                if A[p] == 0:
                    break
                p += 1
            if p == len(A):
                return ans
            elif len(A) - p < K:
                return -1
            else:
                ans += 1
                flips^=1
                A[p] ^= flips
                end_points.append(p + K)
                p += 1


A = [0, 1, 0]
K = 1
A = [1, 1, 0]
K = 2
A = [0, 0, 0, 1, 0, 1, 1, 0]
K = 3
# K=15295

print(Solution().minKBitFlips(A, K))
