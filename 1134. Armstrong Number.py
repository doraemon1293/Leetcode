class Solution:
    def isArmstrong(self, N: int) -> bool:
        return sum([int(x)**len(str(N)) for x in str(N)])==N