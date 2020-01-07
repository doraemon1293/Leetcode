# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        pa, pb = 0, 0
        ans = []
        while pa < len(A) and pb < len(B):
            a = A[pa]
            b = B[pb]
            st = max(a.start, b.start)
            end = min(a.end, b.end)
            if st <= end:
                ans.append(Interval(s=st, e=end))
            if a.end > b.end:
                pb += 1
            elif a.end < b.end:
                pa += 1
            else:
                pa += 1
                pb += 1
        return ans


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
Solution().intervalIntersection(A, B)
