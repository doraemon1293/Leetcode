class Solution:
    def numWays(self, s: str) -> int:
        total = s.count("1")
        if total == 0:
            return (1 + (len(s) - 2)) * (len(s) - 2) // 2 % (10 ** 9 + 7)

        if total % 3:
            return 0
        ones = 0
        p1 = p2 = p3 = p4 = None

        for i in range(len(s)):
            if s[i] == "1":
                ones += 1
            if p1 == None and ones == total // 3:
                p1 = i
            if p2 == None and ones == total // 3 + 1:
                p2 = i
            if p3 == None and ones == (total // 3) * 2:
                p3 = i
            if p4 == None and ones == (total // 3) * 2 + 1:
                p4 = i
        return (p2 - p1) * (p4 - p3) % (10 ** 9 + 7)

