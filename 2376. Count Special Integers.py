import math


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        n+=1
        ans = 0
        str_n = str(n)
        for i in range(1, len(str_n)):
            ans += 9 * math.perm(9, i - 1)
        used = set()
        for i, digit in enumerate(str_n):
            digit = int(digit)
            for d in range(0, digit):
                if (d not in used) and (not (d == 0 and i == 0)):
                    ans += math.perm(9 - len(used), len(str_n) - i - 1)
            if digit in used:
                break
            used.add(digit)

        return ans
