class Solution:
    def tictactoe(self, moves: list) -> str:
        def f(arrs):
            f = False
            for i in range(3):
                if all([x == "X" for x in arrs[i]]):
                    return "A"
                if all([x == "O" for x in arrs[i]]):
                    return "B"
                if all([x == "X" for x in list(zip(*arrs))[i]]):
                    return "A"
                if all([x == "O" for x in list(zip(*arrs))[i]]):
                    return "B"
                if " " in arrs[i]:
                    f = True
            if all([x == "X" for x in [arrs[0][0], arrs[1][1], arrs[2][2]]]):
                return "A"
            if all([x == "O" for x in [arrs[0][0], arrs[1][1], arrs[2][2]]]):
                return "B"
            if all([x == "X" for x in [arrs[0][2], arrs[1][1], arrs[2][0]]]):
                return "A"
            if all([x == "O" for x in [arrs[0][2], arrs[1][1], arrs[2][0]]]):
                return "B"
            return "Pending" if f else "Draw"

        arrs = [[" "] * 3 for _ in range(3)]
        for i in range(len(moves)):
            x, y = moves[i]
            p = "X" if i % 2 == 0 else "O"
            arrs[x][y] = p
        for x in arrs:
            print(x)
        return f(arrs)


moves = [[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]
print(Solution().tictactoe(moves))
