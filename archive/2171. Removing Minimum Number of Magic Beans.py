class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        summ = sum(beans)
        ans = float("inf")
        removed = 0
        N = len(beans)
        for bean in beans:
            ans = min(ans, removed + summ - bean * N)
            removed += bean
            summ -= bean
            N -= 1
        return ans
