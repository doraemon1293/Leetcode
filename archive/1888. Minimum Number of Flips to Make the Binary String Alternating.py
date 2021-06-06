class Solution:
    def minFlips(self, s: str) -> int:
        def diff(s):
            res = float("inf")
            for start in ("0", "1"):
                c = 0
                for i in range(len(s)):
                    if s[i] != start:
                        c += 1
                    start = "0" if start == "1" else "1"
                res = min(c, res)
            return res

        if len(s) % 2 == 0:
            return diff(s)
        else:
            left = [[0, 0] for _ in range(len(s) + 1)]
            for i in range(len(s)):
                if s[i] == "0":
                    left[i + 1][0] = left[i][1]
                    left[i + 1][1] = left[i][0] + 1
                else:
                    left[i + 1][0] = left[i][1] + 1
                    left[i + 1][1] = left[i][0]
            right = [[0, 0] for _ in range(len(s) + 1)]
            for i in range(len(s) - 1, -1, -1):
                if s[i] == "0":
                    right[i][0] = right[i + 1][1]
                    right[i][1] = right[i + 1][0] + 1
                else:
                    right[i][0] = right[i + 1][1] + 1
                    right[i][1] = right[i + 1][0]
            ans = float("inf")
            for i in range(len(s) + 1):
                ans = min(ans, min(left[i]) + min(right[i]))

            return ans