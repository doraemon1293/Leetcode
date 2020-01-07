class Solution:
    def longestDecomposition(self, text: str) -> int:
        self.memo = {}

        def dp(i, j):
            if (i, j) in self.memo:
                return self.memo[i, j]

            if i > j:
                return 0
            if i == j:
                return 1
            k = 1
            temp = 1
            while i + k - 1 < j - k + 1:
                if text[i:i + k] == text[j - k + 1:j + 1]:
                    temp = max(temp, 2 + dp(i + k, j - k))
                k += 1
            self.memo[i, j] = temp
            return temp

        return dp(0, len(text) - 1)




