class Solution:
    def maximizeSweetness(self, sweetness: list, K: int) -> int:
        def ok(mini):
            temp = mini
            k = K + 1
            for n in sweetness:
                temp -= n
                if temp <= 0:
                    k -= 1
                    if k == 0:
                        break
                    temp = mini
            return k == 0

        lo, hi = min(sweetness), sum(sweetness) // (K + 1) + 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = max(ans, mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return ans


sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2]
K = 2
print(Solution().maximizeSweetness(sweetness, K))
