class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif M == 2:
            if Y % 400 == 0:
                return 29
            elif Y % 100 == 0:
                return 28
            elif Y % 4 == 0:
                return 29
            else:
                return 28
        else:
            return 30
