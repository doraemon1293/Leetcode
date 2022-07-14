class Solution:
    def countEven(self, num: int) -> int:
        return sum([sum([int(ch) for ch in str(x)]) % 2 == 0 for x in range(1, num + 1)])
