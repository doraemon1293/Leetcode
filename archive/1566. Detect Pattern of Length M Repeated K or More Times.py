from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        seq = set()
        for i in range(len(arr) - m + 1):
            seq.add(tuple(arr[i:i + m]))

        for s in seq:
            for i in range(len(arr)):
                ii = i
                K = k

                while ii < len(arr) and K and tuple(arr[ii:ii + m]) == s:
                    ii += m
                    K -= 1
                if K == 0:
                    return True

        return False
