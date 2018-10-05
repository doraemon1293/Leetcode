class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ans = [(r0, c0)]
        length = 1
        direction = 0
        while len(ans) < R * C:
            for _ in range(2):
                for __ in range(length):
                    dr, dc = directions[direction]
                    r0 += dr
                    c0 += dc
                    if 0 <= r0 < R and 0 <= c0 < C:
                        print(r0,c0)
                        ans.append((r0, c0))
                direction = (direction + 1) % 4
            length += 1
        return ans


R, C, r0, c0 = 1, 4, 0, 0
print(Solution().spiralMatrixIII(R, C, r0, c0))
