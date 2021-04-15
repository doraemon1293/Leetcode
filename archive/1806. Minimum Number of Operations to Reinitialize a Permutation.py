class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        ans = 0
        arr=list(range(n))
        while ans==0 or arr!=perm:
            ans += 1
            arr = [(arr[i // 2]) if i % 2 == 0 else (arr[n // 2 + (i - 1) // 2]) for i in range(n)]
        return ans
print(Solution().reinitializePermutation(4))