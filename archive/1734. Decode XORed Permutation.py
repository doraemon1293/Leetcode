from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        x = 0
        N = len(encoded) + 1
        for i in range(1, N + 1):
            x ^= i
        y = 0
        for i in range(1, len(encoded), 2):
            y ^= encoded[i]
        arr = [x ^ y]
        for x in encoded:
            arr.append(arr[-1] ^ x)
        return arr
