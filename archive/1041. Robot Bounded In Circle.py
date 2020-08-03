class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        turn = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 0->N 1->W 2->S 3->E
        cur = (0, 0, 0)
        for ch in instructions:
            if ch == "G":
                d = cur[2]
                cur = (cur[0] + turn[d], cur[1] + turn[d], d)
            if ch == "L":
                cur = (cur[0], cur[1], (cur[2] + 1) % 4)
            if ch == "R":
                cur = (cur[0], cur[1], (cur[2] + 3) % 4)
        if (cur[0],cur[1])!=(0,0) and cur[2]==0:
            return False
        else:
            return True