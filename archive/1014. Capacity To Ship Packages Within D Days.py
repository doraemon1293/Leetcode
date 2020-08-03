class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            d = 1
            mid = (left + right) // 2
            remain = mid
            for w in weights:
                if remain >= w:
                    remain -= w
                else:
                    d += 1
                    remain = mid - w
                    if d > D:
                        left = mid + 1
                        break
            if d <= D:
                right = mid
        return left
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(Solution().shipWithinDays(weights,D))