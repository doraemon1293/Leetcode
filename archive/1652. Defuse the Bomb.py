from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = [0] * len(code)
        N = len(code)
        for i in range(N):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    ans[i] += code[j % N]
            if k < 0:
                for j in range(i - 1, i + k - 1,-1):
                    ans[i] += code[j % N]

        return ans