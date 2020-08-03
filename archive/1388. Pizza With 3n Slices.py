from typing import List

import functools


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(i, j, k):
            if j - i + 1 <= 2:
                if k == 0:
                    return 0
                elif k == 1:
                    return max(A[i:j + 1])
                else:
                    return -float('inf')
            return max(dp(i + 2, j, k - 1) + slices[i], dp(i + 1, j, k))

        k = len(slices) // 2
        return max(dp(0, len(slices) - 2, k), dp(1, len(slices) - 1, k))
