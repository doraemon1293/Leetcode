class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        left_days = n % 7
        ans = (28 + (weeks + 3) * 7) * weeks // 2
        ans += ((weeks + 1) + (weeks + left_days)) * left_days // 2
        return ans
