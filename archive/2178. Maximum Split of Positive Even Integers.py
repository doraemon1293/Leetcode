class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        else:
            finalSum //= 2
            n = int((-1 + (1 + 8 * finalSum) ** 0.5) // 2)
            summ = (1 + n) * n // 2
            last = n + finalSum - summ
            ans = [x * 2 for x in list(range(1, n)) + [last]]
            return ans
