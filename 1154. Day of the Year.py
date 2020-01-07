class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = [int(x) for x in date.split("-")]
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y % 400 == 0:
            days[1] = 29
        elif y % 100 == 0:
            pass
        elif y % 4 == 0:
            days[1] = 29
        return sum(days[:m])+d