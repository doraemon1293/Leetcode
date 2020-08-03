class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return int(sum([int(x) for x in str(min(A))])%2==0)
