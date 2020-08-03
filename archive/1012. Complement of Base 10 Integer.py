class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N==0: return 1
        arr = []
        while N:
            arr.append(int(N % 2) ^ 1)
            N //= 2
        print(arr)
        base = 1
        ans = 0
        for a in arr:
            ans += a * base
            base *= 2
        return ans


print(Solution().bitwiseComplement(8))
