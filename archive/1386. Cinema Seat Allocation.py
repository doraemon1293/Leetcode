from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        reservedSeats.extend([[n + 1, i] for i in range(1, 11)])
        ans = 0
        cur_r = 1
        seats = [True] * 3
        for r, c in reservedSeats:
            if r > cur_r:
                if seats[0] and seats[2]:
                    ans += 2
                elif seats[0] or seats[1] or seats[2]:
                    ans += 1
                ans += (r - cur_r - 1) * 2
                cur_r = r
                seats = [True] * 3
            if c in (2, 3, 4, 5):
                seats[0] = False
            if c in (4, 5, 6, 7):
                seats[1] = False
            if c in (6, 7, 8, 9):
                seats[2] = False

        return ans


n = 20
reservedSeats = [[2, 1], [1, 8], [2, 6]]
print(Solution().maxNumberOfFamilies(n, reservedSeats))
