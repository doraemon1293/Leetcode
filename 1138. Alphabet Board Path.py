class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = {}
        for i in range(26):
            x = i // 5
            y = i % 5
            board[chr(ord("a") + i)] = (x, y)
        ch1 = "a"
        print(board)

        def go(ch1, ch2):
            x1, y1 = board[ch1]
            x2, y2 = board[ch2]
            if ch1 == "z":
                return ["U" if x1 > x2 else "D"] * int(abs(x1 - x2)) + ["L" if y1 > y2 else "R"] * int(abs(y1 - y2)) + ["!"]
            else:
                return ["L" if y1 > y2 else "R"] * int(abs(y1 - y2)) + ["U" if x1 > x2 else "D"] * int(abs(x1 - x2)) + ["!"]

        ans = []
        for ch in target:
            ans += go(ch1, ch)
            ch1 = ch
        return "".join(ans)


target = "leet"
print(Solution().alphabetBoardPath(target))
