import collections


class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        return self.subarraysWithMostKDistinct(A,K)-self.subarraysWithMostKDistinct(A,K-1)

    def subarraysWithMostKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        left = right = 0
        d = collections.defaultdict(int)
        count = 0
        res=0
        while right < len(A):
            d[A[right]] += 1
            if d[A[right]] == 1:
                count += 1
            right += 1
            while left < right and count > K:
                d[A[left]] -= 1
                if d[A[left]] == 0:
                    count -= 1
                left += 1
            res += right - left
        return res
