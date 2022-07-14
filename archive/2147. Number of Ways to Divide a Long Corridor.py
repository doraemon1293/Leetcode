class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = corridor.count("S")
        if seats == 0 or seats % 2:
            return 0

        ans = 1
        seat = 0
        last_seat = None
        MOD = 10 ** 9 + 7
        for i, ch in enumerate(corridor):
            if ch == "S":
                if seat < 2:
                    seat += 1
                    last_seat = i
                else:
                    ans = (ans * (i - last_seat)) % MOD
                    seat = 1
                    last_seat = i
        return ans
