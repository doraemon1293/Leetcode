class Solution:
    def minOperations(self, n: int) -> int:
        return sum([abs(n - i) for i in range(1, 2 * n + 1, 2)]) // 2

